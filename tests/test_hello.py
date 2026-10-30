# tests/test_hello.py
"""Test case for hello.py application."""
import sys
from pathlib import Path

# Add project root directory to sys.path so hello.py can be imported directly
PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from hello import get_message, main


def test_hello_mlops_message(capsys):
    """Test 1: Verify get_message returns expected greeting and main prints it."""
    # Test function return value
    message = get_message()
    print(f"\n[PYTEST OUTPUT] get_message() returned: '{message}'")
    assert message == "Hello MLOps", f"Expected 'Hello MLOps', got '{message}'"

    # Test main() execution and standard output
    main()
    captured = capsys.readouterr()
    print(f"[PYTEST OUTPUT] captured stdout from main(): '{captured.out.strip()}'")
    assert "Hello MLOps" in captured.out
