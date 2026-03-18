import typer
from forge.core.prompts import ask_project_type, ask_test_library
from forge.core.runner import run_command
from forge.core.templates import create_template

def new(
    project_name: str = typer.Argument(None, help="Name of the project to create")
):
    """Create a new Python project."""

    if not project_name:
        project_name = typer.prompt("Project name")

    project_type = ask_project_type()
    test_library = ask_test_library()

    run_command(project_name, project_type, test_library)
    create_template(project_name, project_type, test_library)