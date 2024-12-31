from app.commands.general.hello import hello_command
from app.commands.management.add import add_entry
from app.commands.management.update import update_entry
from app.commands.management.delete import delete_entry
from app.commands.general.list_all import list_entries
import click

@click.group()
def cli():
    pass

cli.add_command(hello_command)
cli.add_command(add_entry)
cli.add_command(update_entry)
cli.add_command(delete_entry)
cli.add_command(list_entries)

if __name__ == '__main__':
    cli()