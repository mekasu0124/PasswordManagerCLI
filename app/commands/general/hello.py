import click


@click.command(name="hello")
@click.option("--name", default="User", help="Enter the name you want the system to greet you by")
def hello_command(name: str) -> None:
    """
    The hello_command greets the user given that a name
    is provided, otherwise, uses the default value for
    the user's name.
    """
    return click.echo(f"Hello, {name}! Welcome To Mek's Hub Password Manager CLI App!")