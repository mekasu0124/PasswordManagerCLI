import click


@click.command(name="hello")
@click.option("--name", default="User", help="Enter the name you want the system to greet you by")
def hello_command(name: str) -> None:
    """
    The hello_command greets the user given that a name
    is provided, otherwise, uses the default value for
    the user's name.
    """

    msg = (
        f"Hello, {name}!\n"
        "This message shows that your installation worked! Yay!\n"
        "\n"
        "App Name: Mek's Hub Password Manager - CLI\n"
        "App Version: 1.0.0\n"
        "App Description: A light-weight cli application to assist in storing your passwords for easier use and lookup. Most password managers are behind multiple screen options, so why not have one that is just as simple as pwm lookup --link your_link_here or pwm add --link your_link --username your_username --password your_password to have your information readily available."
    )
    return click.echo(msg)