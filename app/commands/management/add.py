import click


@click.command(name="add")
@click.option("--password", help="The password you want the program to save.")
def add_pw_command(name: str) -> None:
    

    return click.echo(f"Hello, {name}! Welcome To Mek's Hub Password Manager CLI App!")