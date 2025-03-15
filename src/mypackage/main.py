"""
Main module for the application.
"""

import sys
from typing import List, Optional


def greet(name: Optional[str] = None) -> str:
    """
    Return a greeting message.
    
    Args:
        name: The name to greet. If None, a generic greeting is returned.
        
    Returns:
        A greeting message.
    """
    if name:
        return f"Hello, {name}! Welcome to this UV-managed Python project."
    return "Hello, world! Welcome to this UV-managed Python project."


def main(args: List[str] = None) -> int:
    """
    Main entry point for the application.
    
    Args:
        args: Command line arguments (defaults to sys.argv[1:])
        
    Returns:
        Exit code.
    """
    if args is None:
        args = sys.argv[1:]
    
    name = args[0] if args else None
    print(greet(name))
    
    return 0


if __name__ == "__main__":
    sys.exit(main())