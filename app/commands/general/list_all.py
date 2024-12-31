from app.utilities.json import JsonEngine
import click
from rich.console import Console
from rich.table import Table

console = Console()

@click.command(name="list")
def list_entries():
    json_engine = JsonEngine()
    all_entries = json_engine.list_all_entries()

    if not all_entries:
        console.print("[bold #272123]No entries found![/bold #272123]")
        return

    table = Table(
        title="[bold #849da2]All Entries[/bold #849da2]",
        show_header=True,
        header_style="bold #385d8d",
        border_style="#385d8d"
    )
    table.add_column("Link", style="#2dc0f1", no_wrap=True)
    table.add_column("Username", style="#272123")
    table.add_column("Password", style="#c32b37")

    for entry in all_entries:
        table.add_row(entry["link"], entry["username"], entry["password"])

    console.print(table)