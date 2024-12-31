from click.testing import CliRunner
from app.commands.management.update import update_command

def test_update_command():
    runner = CliRunner()

    result = runner.invoke(
        update_command,
        ["--link", "https://google.com", "--username", "mekasu012444", "--password", "Test123!", "--new-username", "mekasu0124", "--new-password", "Test1234!"]
    )

    assert result.exit_code == 0
    assert "Entry Updated" in result.output or "Entry not found" in result.output