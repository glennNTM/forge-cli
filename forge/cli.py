import typer
import pyfiglet
from rich.console import Console
from rich.text import Text
from rich.panel import Panel
from rich.align import Align

from forge.commands.new import new

app = typer.Typer(
    name="forge",
    help="[bold #64DD17]Forge CLI[/] — Modern Python project scaffolding",
    add_completion=False,
    rich_markup_mode="rich", 
)

console = Console()

def hex_to_rgb(hex_color: str) -> tuple:
    hex_color = hex_color.lstrip("#")
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def interpolate_color(color1: str, color2: str, t: float) -> str:
    r1, g1, b1 = hex_to_rgb(color1)
    r2, g2, b2 = hex_to_rgb(color2)
    r = int(r1 + (r2 - r1) * t)
    g = int(g1 + (g2 - g1) * t)
    b = int(b1 + (b2 - b1) * t)
    return f"#{r:02X}{g:02X}{b:02X}"

def apply_horizontal_gradient(line: str, colors: list) -> Text:
    text = Text()
    # Après
    total = sum(1 for c in line if c != " ")

    if total == 0:
        text.append(line)
        return text

    visible_index = 0
    num_segments = len(colors) - 1

    for char in line:
        if char == " ":
            text.append(" ")
        else:
            t = visible_index / max(total - 1, 1)
            segment = min(int(t * num_segments), num_segments - 1)
            local_t = (t * num_segments) - segment
            color = interpolate_color(colors[segment], colors[segment + 1], local_t)
            text.append(char, style=f"bold {color}")
            visible_index += 1

    return text

def print_banner():
    ascii_art = pyfiglet.figlet_format("FORGE", font="doom")
    lines = ascii_art.splitlines()

    gradient_colors = [
        "#B2FF59",
        "#76FF03",
        "#64DD17",
        "#00C853",
        "#00B050",
        "#007E33",
    ]

    for line in lines:
        console.print(apply_horizontal_gradient(line, gradient_colors))

    console.print(Text(" Modern Python project scaffolding", style="italic #64DD17"))
    console.print()


@app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    if ctx.invoked_subcommand is None:
        print_banner()
        
        # Updated panel text colors
        welcome_msg = (
            "Welcome to [bold #76FF03]Forge[/]!\n\n"
            "To create a new project, run:\n"
            "[bold #00C853]forge new <project_name>[/]"
        )
        
        panel = Panel(
            Align.left(welcome_msg), 
            border_style="#007E33", 
            padding=(1, 4),
            title="[dim]Getting Started[/dim]",
            title_align="left"

        )
        
        console.print(panel)
        console.print()

# Updated command help color
app.command("new", help="Scaffold a [bold #64DD17]new project[/] from a template")(new)

if __name__ == "__main__":
    app()