from typer import Typer
from session_9.bot import *
import os
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO,
                    format="[%(filename)s] - [%(funcName)s]")

app = Typer()


@app.command()
def eticbot():
    logging.info("Bot ON")
    return client.run(os.getenv('DISCORD_TOKEN', None))

if __name__ == "__main__":
    app()
