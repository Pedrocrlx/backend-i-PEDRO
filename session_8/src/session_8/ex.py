from typer import Typer
import logging
from rich import print

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO,
                    format="[%(filename)s] - [%(funcName)s]")

app = Typer()


@app.command()
def SquareNumber(num: int) -> int:
    print("[bold red]Vai Jorge ![/bold red]")
    logger.info("Square Number")
    result = 0
    result = num ** 2
    print(result)


if __name__ == "__main__":
    app()
