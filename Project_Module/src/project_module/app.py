import typer

app = typer.Typer()

@app.command()
def Add_Event(name: str, date: str, location: str, description: str = typer.Option("", help="Description of Event")):
    """
    Add a new Event.
    """
    event = {
        "name": name,
        "date": date,
        "location": location,
        "description": description,
    }

    print(f"Event was successfully added: {event}")

if __name__ == "__main__":
    app()
