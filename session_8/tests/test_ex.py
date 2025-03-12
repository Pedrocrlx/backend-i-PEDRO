from typer.testing import CliRunner
from src.session_8.challenge import app

runner = CliRunner()


def test_squareNumber():
    result = runner.invoke(app, ["squarenumber", "4"])
    assert result.exit_code == 0
    assert result.output.strip() == "Square of 4 is 16"
