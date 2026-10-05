"""A small, repeatable CSV-to-SQLite batch pipeline using only the stdlib.

Run from the repository root with:
    python -m data_engineering.batch_pipeline
"""

import argparse
import csv
import logging
import sqlite3
from dataclasses import dataclass
from pathlib import Path

from .validation import InvalidOrder, Order, parse_order

logger = logging.getLogger(__name__)
DEFAULT_INPUT = (
    Path(__file__).parent.parent / "data_engineering" / "pandas" / "sample_data" / "orders.csv"
)
DEFAULT_DATABASE = Path(__file__).parent / "orders.sqlite3"


@dataclass(frozen=True)
class LoadSummary:
    read: int
    loaded: int
    rejected: int


def read_orders(source: Path) -> tuple[list[Order], list[str]]:
    """Extract CSV rows, validate them, and retain row-level rejection reasons."""
    accepted: list[Order] = []
    rejected: list[str] = []

    with source.open(newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)
        required = {"OrderID", "CustomerName", "Product", "Quantity", "Price", "OrderDate"}
        if reader.fieldnames is None or not required.issubset(reader.fieldnames):
            raise ValueError(f"CSV must contain these columns: {', '.join(sorted(required))}")

        for line_number, row in enumerate(reader, start=2):
            try:
                accepted.append(parse_order(row))
            except InvalidOrder as error:
                rejected.append(f"line {line_number}: {error}")

    return accepted, rejected


def load_orders(database: Path, orders: list[Order]) -> int:
    """Load using a transaction and an order ID key so reruns are idempotent."""
    database.parent.mkdir(parents=True, exist_ok=True)
    with sqlite3.connect(database) as connection:
        connection.execute("PRAGMA foreign_keys = ON")
        connection.execute(
            """CREATE TABLE IF NOT EXISTS orders (
                order_id INTEGER PRIMARY KEY,
                customer_name TEXT NOT NULL,
                product TEXT NOT NULL,
                quantity INTEGER NOT NULL CHECK (quantity > 0),
                unit_price_cents INTEGER NOT NULL CHECK (unit_price_cents >= 0),
                order_date TEXT NOT NULL
            )"""
        )
        connection.executemany(
            """INSERT INTO orders
                (order_id, customer_name, product, quantity, unit_price_cents, order_date)
                VALUES (?, ?, ?, ?, ?, ?)
                ON CONFLICT(order_id) DO UPDATE SET
                    customer_name = excluded.customer_name,
                    product = excluded.product,
                    quantity = excluded.quantity,
                    unit_price_cents = excluded.unit_price_cents,
                    order_date = excluded.order_date""",
            [
                (order.order_id, order.customer_name, order.product, order.quantity,
                 order.unit_price_cents, order.order_date.isoformat())
                for order in orders
            ],
        )
        return connection.execute("SELECT COUNT(*) FROM orders").fetchone()[0]


def revenue_by_product(database: Path) -> list[tuple[str, int]]:
    """Use SQL aggregation to return each product's revenue in cents."""
    with sqlite3.connect(database) as connection:
        return connection.execute(
            """SELECT product, SUM(quantity * unit_price_cents) AS revenue_cents
               FROM orders
               GROUP BY product
               ORDER BY revenue_cents DESC, product"""
        ).fetchall()


def run_pipeline(source: Path, database: Path) -> LoadSummary:
    """Run extract, validate, load, and report stages for a single batch."""
    orders, rejected = read_orders(source)
    total_in_database = load_orders(database, orders)
    summary = LoadSummary(len(orders) + len(rejected), len(orders), len(rejected))

    logger.info(
        "Batch complete: read=%d loaded=%d rejected=%d total_in_database=%d",
        summary.read, summary.loaded, summary.rejected, total_in_database,
    )
    for reason in rejected:
        logger.warning("Rejected %s", reason)
    for product, revenue_cents in revenue_by_product(database):
        logger.info("Product revenue: %s = $%d.%02d", product, *divmod(revenue_cents, 100))
    return summary


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT, help="source CSV path")
    parser.add_argument("--database", type=Path, default=DEFAULT_DATABASE, help="SQLite output path")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    run_pipeline(args.input, args.database)


if __name__ == "__main__":
    main()
