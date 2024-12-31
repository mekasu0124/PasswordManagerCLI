

from app.commands.general.hello import hello_command
from app.commands.management.add import add_pw_command

import click


class PasswordManagerCLI:
    def __init__(self):
        self.cli_group = click.Group(
            name="Password Manager CLI",
            help="A Password Manager CLI Application\n\nUse the commands below to interact with the application"
        )
        self.register_commands()
        self.setup_db()

    def register_commands(self):
        """Register all commands to the CLI group."""
        self.cli_group.add_command(hello_command)
        self.cli_group.add_command(add_pw_command)

    def run(self):
        """Run the CLI application."""
        self.cli_group()


def main():
    app = PasswordManagerCLI()
    app.run()

if __name__ == '__main__':
    main()