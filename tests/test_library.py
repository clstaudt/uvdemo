"""Tests for uvdemo.library module."""

from io import StringIO
from rich.console import Console
from uvdemo.library import output_greeting, output_table


def test_output_greeting():
    """Test that output_greeting produces output without errors."""
    console = Console(file=StringIO())
    output_greeting(console)
    # If we get here without exception, the test passes


def test_output_table():
    """Test that output_table produces output without errors."""
    console = Console(file=StringIO())
    output_table(console)
    # If we get here without exception, the test passes

