from click.testing import CliRunner
from app.commands.management.add import add_pw_command

def test_add_command():
    runner = CliRunner()

    # Correctly pass all arguments and options in a single list
    result = runner.invoke(
        add_pw_command,
        ["--link", "https://google.com", "--username", "mekasu0124", "--password", "Test123!"],
        input="y"
    )

    assert result.exit_code == 0
    # Optionally, you can also check the output to ensure it's correct
    assert "Data Saved" in result.output
