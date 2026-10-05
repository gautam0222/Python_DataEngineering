"""Functions, explicit arguments, and lazy iteration for larger inputs."""

from collections.abc import Iterable, Iterator


def normalize_name(name: str, *, uppercase: bool = False) -> str:
    """Normalize whitespace; ``uppercase`` is deliberately keyword-only."""
    normalized = " ".join(name.split())
    return normalized.upper() if uppercase else normalized.title()


def batches(items: Iterable[str], size: int) -> Iterator[list[str]]:
    """Yield fixed-size batches without materializing the whole input."""
    if size <= 0:
        raise ValueError("size must be greater than zero")

    batch: list[str] = []
    for item in items:
        batch.append(item)
        if len(batch) == size:
            yield batch
            batch = []

    if batch:
        yield batch


def main() -> None:
    customers = (f" customer {number} " for number in range(1, 8))
    for batch_number, batch in enumerate(batches(customers, 3), start=1):
        names = [normalize_name(name) for name in batch]
        print(f"Batch {batch_number}: {names}")


if __name__ == "__main__":
    main()
