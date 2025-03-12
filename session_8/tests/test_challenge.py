from typer.testing import CliRunner
from src.session_8.challenge import app

runner = CliRunner()


def test_sum():
    result = runner.invoke(app, ["sum", "3", "5"])
    assert result.exit_code == 0
    assert result.output.strip() == "3 + 5 = 8"

def test_subtraction():
    result = runner.invoke(app, ["subtraction", "10", "4"])
    assert result.exit_code == 0
    assert result.output.strip() == "10 - 4 = 6"

def test_squareNumber():
    result = runner.invoke(app, ["squarenumber", "4"])
    assert result.exit_code == 0
    assert result.output.strip() == "Square of 4 is 16"
