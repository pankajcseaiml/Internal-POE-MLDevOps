# hello.py
"""Simple single file application for beginner MLOps pipeline."""


def get_message() -> str:
    """Return the welcome message."""
    return "Hello MLOps"


def main():
    """Print the welcome message for the project."""
    message = get_message()
    print(message)


if __name__ == "__main__":
    main()
