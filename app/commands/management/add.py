from app.utilities.json import JsonEngine
import click
from rich.console import Console

console = Console()

@click.command(name="add")
@click.option("--link", required=True, help="The link associated with the password.")
@click.option("--username", required=True, help="The username associated with the password.")
@click.option("--password", required=True, help="The password you want to save.")
def add_entry(link: str, username: str, password: str):
    json_engine = JsonEngine()
    data_to_save = {
        "link": link,
        "username": username,
        "password": password
    }
    result = json_engine.save_entry(data_to_save)
    console.print(f"[bold #385d8d]{result}[/bold #385d8d]")