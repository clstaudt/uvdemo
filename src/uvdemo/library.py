"""Library module for uvtest containing reusable functions."""

from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.table import Table
from halo import Halo
import time



def output_greeting(console: Console) -> None:
    """Output a bold green greeting inside a Panel."""
    greeting = Text("Hello from uvdemo!", style="bold green")
    console.print(Panel(greeting, title="uvdemo"))


def output_table(console: Console) -> None:
    """Output an example Table."""
    table = Table(title="Demo table")
    table.add_column("Name", style="cyan", no_wrap=True)
    table.add_column("Value", justify="right", style="magenta")
    table.add_row("A", "42")
    table.add_row("B", "7")
    console.print(table)

def work_work(console: Console) -> None:
    """Display a halo spinner for 3 seconds and then say done."""
    spinner = Halo(text='Working...', spinner='dots')
    spinner.start()
    time.sleep(3)
    spinner.succeed('Done!')