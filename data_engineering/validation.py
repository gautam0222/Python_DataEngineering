"""Parse and validate order records at a data pipeline's boundary."""

from dataclasses import dataclass
from datetime import date
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP

SQLITE_INTEGER_MAX = 2**63 - 1


@dataclass(frozen=True)
class Order:
    order_id: int
    customer_name: str
    product: str
    quantity: int
    unit_price_cents: int
    order_date: date


class InvalidOrder(ValueError):
    """Raised when a source row cannot be represented as a valid order."""


def parse_order(row: dict[str, str]) -> Order:
    """Validate a CSV row and convert it to a typed, normalized record."""
    try:
        order_id = int(row["OrderID"])
        quantity = int(row["Quantity"])
        price = Decimal(row["Price"])
        order_date = date.fromisoformat(row["OrderDate"])
    except (KeyError, TypeError, ValueError, InvalidOperation) as error:
        raise InvalidOrder(f"invalid or missing field: {error}") from error

    customer_name = " ".join((row.get("CustomerName") or "").split())
    product = " ".join((row.get("Product") or "").split())

    if order_id <= 0:
        raise InvalidOrder("OrderID must be positive")
    if order_id > SQLITE_INTEGER_MAX or quantity > SQLITE_INTEGER_MAX:
        raise InvalidOrder("OrderID and Quantity must fit in a SQLite integer")
    if not customer_name or not product:
        raise InvalidOrder("CustomerName and Product are required")
    if quantity <= 0:
        raise InvalidOrder("Quantity must be positive")
    if not price.is_finite() or price < 0:
        raise InvalidOrder("Price must be a finite, nonnegative number")

    try:
        cents = int((price * 100).quantize(Decimal("1"), rounding=ROUND_HALF_UP))
    except InvalidOperation as error:
        raise InvalidOrder("Price is outside the supported range") from error
    if cents > SQLITE_INTEGER_MAX or cents * quantity > SQLITE_INTEGER_MAX:
        raise InvalidOrder("line-item revenue must fit in a SQLite integer")

    return Order(order_id, customer_name, product, quantity, cents, order_date)
