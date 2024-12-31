import click


@click.command(name="add")
@click.option("--link", required=True, help="The link associated with the password.")
@click.option("--username", required=True, help="The username associated with the password.")
@click.option("--password", help="The password you want to save.")
def add_pw_command(link: str, username: str, password: str) -> None:
    click.echo(f"Data To Save:\n\nLink: {link}\nUsername: {username}\nPassword: {password}")

    user_agree = input("\n\nDo You Approve? (Y/N): ")

    while not user_agree.lower() in ["y","n"]:
        click.echo("Invalid Input. Enter 'Y' for Yes or 'N' for No")

        user_agree = input("\n\nDo You Approve? (Y/N): ")

        if user_agree.lower() in ["y","n"]:
            break

    if user_agree.lower() == "n":
        click.echo("You Disapproved. Please Run The Command Again Later")
        exit(0)

    data_to_save = {
        "link": link,
        "username": username,
        "password": password
    }

    click.echo(f"Data Saved: {data_to_save}")