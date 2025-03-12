from typer import Typer
import logging
from rich import print

app = Typer()

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO,
                    format="[%(filename)s] - [%(funcName)s]")


@app.command()
def squareNumber(num: int) -> int:
    print("[bold red]Vai Jorge ![/bold red]")
    logger.info("Square Number")
    result = 0
    result = num ** 2
    print(f"Square of {num} is {result}")


@app.command()
def Sum(n1: int, n2: int) -> int:
    print("[bold red]Vai Jorge ![/bold red]")
    logger.info("Sum")
    result = 0
    result = n1 + n2
    print(f"{n1} + {n2} = {result}")


@app.command()
def subtraction(n1: int, n2: int) -> int:
    print("[bold red]Vai Jorge ![/bold red]")
    logger.info("Subtraction")
    result = 0
    result = n1 - n2
    print(f"{n1} - {n2} = {result}")


if __name__ == "__main__":
    app()
