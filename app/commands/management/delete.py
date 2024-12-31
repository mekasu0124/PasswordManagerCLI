from app.utilities.json import JsonEngine
import click
from rich.console import Console
from rich.panel import Panel

console = Console()

@click.command(name="delete")
@click.option("--link", required=True, help="The link of the entry to delete")
@click.option("--username", required=True, help="The username of the entry to delete")
def delete_entry(link: str, username: str):
    json_engine = JsonEngine()
    all_entries = json_engine.list_all_entries()
    entry_to_delete = None
    for index, entry in enumerate(all_entries):
        if entry["link"] == link and entry["username"] == username:
            entry_to_delete = entry
            break
    if entry_to_delete:
        panel = Panel(
            f"Found Entry:\n\nLink: {entry_to_delete['link']}\nUsername: {entry_to_delete['username']}\nPassword: {entry_to_delete['password']}",
            title="[bold #1f2f45]Delete Entry[/bold #1f2f45]",
            border_style="#849da2"
        )
        console.print(panel)
        user_agree = input("\nAre You Sure You Want To Delete This Entry? (Y/N): ")
        while not user_agree.lower() in ["y", "n"]:
            console.print("[bold #272123]Invalid Input. Enter 'Y' for Yes or 'N' for No[/bold #272123]")
            user_agree = input("Are You Sure You Want To Delete This Entry? (Y/N): ")
            if user_agree.lower() in ["y", "n"]:
                break
        if user_agree.lower() == 'n':
            console.print("[bold #385d8d]You Elected To Keep This Entry.[/bold #385d8d]")
            return
        result = json_engine.delete_entry(entry_to_delete)
        console.print(f"[bold #385d8d]{result}[/bold #385d8d]")