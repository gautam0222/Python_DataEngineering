"""Exceptions, context managers, and logging for reliable file processing."""

import logging
from pathlib import Path

logger = logging.getLogger(__name__)


def count_nonempty_lines(path: Path) -> int:
    """Count nonblank UTF-8 lines and report useful context on I/O errors."""
    try:
        with path.open(encoding="utf-8") as source:
            return sum(1 for line in source if line.strip())
    except OSError as error:
        logger.exception("Could not read input file %s", path)
        raise RuntimeError(f"Unable to process {path}") from error


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    sample = Path(__file__).with_name("sample.txt")
    try:
        print(f"Nonempty lines: {count_nonempty_lines(sample)}")
    except RuntimeError as error:
        logger.error("%s", error)


if __name__ == "__main__":
    main()
