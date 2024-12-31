from click.testing import CliRunner
from app.commands.management.add import add_command

def test_add_command():
    runner = CliRunner()

    # Correctly pass all arguments and options in a single list
    result = runner.invoke(
        add_command,
        ["--link", "https://google.com", "--username", "mekasu0124", "--password", "Test123!"],
        input="y"
    )

    assert result.exit_code == 0
    assert "Entry Saved" in result.output or "\nEntry Already Exists" in result.output
