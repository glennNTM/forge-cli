import typer

app = typer.Typer(
    name="forge",
    help="🔥 Forge CLI — Modern Python project scaffolding",
    add_completion=False,
)

@app.command()
def new(
    project_name: str = typer.Argument(None, help="Name of the project to create")
):
    """Create a new Python project."""
    typer.echo(f"🔥 Forge CLI — Creating project: {project_name}")

if __name__ == "__main__":
    app()