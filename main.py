"""Simple greeting program used to test the autonomous engineering workflow."""
import sys


def greet(name: str = "World") -> str:
    return f"Hello, {name}!"


def main(argv: list[str] | None = None) -> int:
    args = sys.argv[1:] if argv is None else argv
    print(greet(" ".join(args) if args else "World"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
