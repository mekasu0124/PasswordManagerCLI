from app.utilities.json import JsonEngine

import click


@click.command(name="add")
@click.option("--link", required=True, help="The link associated with the password.")
@click.option("--username", required=True, help="The username associated with the password.")
@click.option("--password", required=True, help="The password you want to save.")
def add_entry(link: str, username: str, password: str):
    """
    Allows the user to save their desired link, username, and password
    """

    json_engine = JsonEngine()

    data_to_save = {
        "link": link,
        "username": username,
        "password": password
    }

    result = json_engine.save_entry(data_to_save)
    return click.echo(result)
