import typer
from forge.commands.new import new

app = typer.Typer(
    name="forge",
    help="Forge CLI — Modern Python project scaffolding",
    add_completion=False,
)

@app.callback()
def main():
    pass

app.command("new")(new)

if __name__ == "__main__":
    app()