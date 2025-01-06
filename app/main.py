from app.commands.general.hello import hello_command
from app.commands.general.list_all import list_entries

from app.commands.management.add import add_entry
from app.commands.management.update import update_entry
from app.commands.management.delete import delete_entry

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
    """
    TODO:

    ?1. Create a check system with the json engine to see if it's the programs first launch
    ?2. If so, launch create new user functionality to allow user to create account
    ?3. Launch program
    """

    cli()