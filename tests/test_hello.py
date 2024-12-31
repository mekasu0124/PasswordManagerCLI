from click.testing import CliRunner
from app.commands.general.hello import hello_command


def test_hello_command():
    runner = CliRunner()

    result = runner.invoke(hello_command, ["--name", "Mek"])

    assert result.exit_code == 0
    assert "Hello, Mek!" in result.output
