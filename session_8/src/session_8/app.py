from typer import Typer

app = Typer()

@app.command()
def cenas():
    print(True)

@app.command()
def cenas2():
    print(False)

if __name__ == "__main__":
    app()
