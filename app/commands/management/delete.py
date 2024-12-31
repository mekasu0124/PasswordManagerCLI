from app.utilities.json import JsonEngine

import click


@click.command(name="delete")
@click.option("--link", required=True, help="The link of the entry to delete")
@click.option("--username", required=True, help="The username of the entry to delete")
def delete_entry(link: str, username: str):
    """
    Allows the user to delete an existing entry from the given link and username.
    """

    json_engine = JsonEngine()

    all_entries = json_engine.list_all_entries()

    entry_to_delete = None

    for index, entry in enumerate(all_entries):
        if entry["link"] == link and entry["username"] == username:
            entry_to_delete = entry
            break
        
    if entry_to_delete:
        click.echo(f"Found Entry:\n\nLink: {entry_to_delete["link"]}\nUsername: {entry_to_delete["username"]}\nPassword: {entry_to_delete["password"]}")
            
        user_agree = input("\nAre You Sure You Want To Delete This Entry? (Y/N): ")

        while not user_agree.lower() in ["y", "n"]:
            click.echo("Invalid Input. Enter 'Y' for Yes or 'N' for No")
            user_agree = input("Are You Sure You Want To Delete This Entry? (Y/N): ")

            if user_agree.lower() in ["y", "n"]:
                break

        if user_agree.lower() == 'n':
            return click.echo("You Elected To Keep This Entry.")
        
        result = json_engine.delete_entry(entry_to_delete)

        return click.echo(result)
