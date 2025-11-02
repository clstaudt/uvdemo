"""Demo using Rich to produce styled console output.

This file demonstrates a minimal usage of `rich` to print a bold green
greeting inside a Panel and an example Table.
"""

from rich.console import Console

from uvtest.library import output_greeting, output_table


def make_demo(console: Console) -> None:
    """Print a small rich demo: Panel + Table."""
    # Output greeting using library function
    output_greeting(console)
    
    # Output table using library function
    output_table(console)


def main() -> None:
    console = Console()
    make_demo(console)


if __name__ == "__main__":
    main() 
