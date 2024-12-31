import click
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()

@click.command(name="hello")
@click.option("--name", default="User", help="Enter the name you want the system to greet you by")
def hello_command(name: str) -> None:
    msg = Text()
    msg.append(f"Hello, {name}!\n", style="bold #385d8d")
    msg.append("This message shows that your installation worked! Yay!\n", style="#4c6770")
    msg.append("\n", style="#849da2")
    msg.append("App Name: Mek's Hub Password Manager - CLI\n", style="bold #1f2f45")
    msg.append("App Version: 1.0.0\n", style="#272123")
    msg.append("App Description: A light-weight CLI application to assist in storing your passwords for easier use and lookup. Most password managers are behind multiple screen options, so why not have one that is just as simple as ", style="#4c6770")
    msg.append("pwm lookup --link your_link_here", style="bold #385d8d")
    msg.append(" or ", style="#4c6770")
    msg.append("pwm add --link your_link --username your_username --password your_password", style="bold #385d8d")
    msg.append(" to have your information readily available.", style="#4c6770")
    panel = Panel(
        msg,
        title="[bold #1f2f45]Welcome to Mek's Hub Password Manager[/bold #1f2f45]",
        border_style="#849da2",
        padding=(1, 2),
    )
    console.print(panel)