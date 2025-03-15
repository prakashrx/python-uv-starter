"""
Tests for the main module.
"""

from mypackage.main import greet, main


def test_greet_with_name() -> None:
    """Test greet function with a name."""
    result = greet("Alice")
    assert "Alice" in result
    assert result == "Hello, Alice! Welcome to this UV-managed Python project."


def test_greet_without_name() -> None:
    """Test greet function without a name."""
    result = greet()
    assert "world" in result
    assert result == "Hello, world! Welcome to this UV-managed Python project."


def test_main_with_name(capsys) -> None:
    """Test main function with a name."""
    exit_code = main(["Bob"])
    captured = capsys.readouterr()
    
    assert exit_code == 0
    assert "Bob" in captured.out
    assert captured.out.strip() == "Hello, Bob! Welcome to this UV-managed Python project."


def test_main_without_name(capsys) -> None:
    """Test main function without a name."""
    exit_code = main([])
    captured = capsys.readouterr()
    
    assert exit_code == 0
    assert "world" in captured.out
    assert captured.out.strip() == "Hello, world! Welcome to this UV-managed Python project."