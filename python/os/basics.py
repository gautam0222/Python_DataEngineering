from pathlib import Path


def main() -> None:
    lesson_dir = Path(__file__).resolve().parent
    print("Working directory:", Path.cwd())
    print("Lesson file:", Path(__file__).resolve())
    print("Lesson folder:", lesson_dir)

    for path in lesson_dir.iterdir():
        kind = "directory" if path.is_dir() else "file"
        print(f"{path.name} is a {kind}")

    sample_child = lesson_dir / "sample_data"
    print("Joined path:", sample_child)
    if sample_child.is_dir():
        print("Sample folder contents:", [path.name for path in sample_child.iterdir()])
    else:
        print("Create a sample_data folder beside this file to inspect its contents.")


if __name__ == "__main__":
    main()
