from app.commands.general.hello import hello_command
from app.commands.management.add import add_entry
from app.commands.management.update import update_command

import click


@click.group()
def cli():
    """
    A Password Manager CLI Application

    Use the commands below to interact with the application
    """
    pass

cli.add_command(hello_command)
cli.add_command(add_entry)
cli.add_command(update_command)


if __name__ == '__main__':
    cli()