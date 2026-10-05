"""Small examples of Python's built-in collection types and comprehensions."""

from collections import Counter


def summarize_words(words: list[str]) -> dict[str, int]:
    """Return word counts while demonstrating list, set, and dict usage."""
    cleaned = [word.strip().lower() for word in words if word.strip()]
    unique_words = set(cleaned)
    counts = Counter(cleaned)
    return {word: counts[word] for word in sorted(unique_words)}


def main() -> None:
    words = ["Python", "data", "Python", "engineering", "data"]
    print("Original order:", words)  # list: ordered and mutable
    print("First item:", words[0])

    coordinates = (12.9, 77.6)  # tuple: ordered and immutable
    print("Coordinates:", coordinates)

    print("Unique words:", set(words))  # set: unique values, no ordering guarantee
    print("Word counts:", summarize_words(words))  # dict: key/value mapping


if __name__ == "__main__":
    main()
