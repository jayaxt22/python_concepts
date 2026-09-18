
import time

from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.progress import track
from rich.markdown import Markdown
from rich.syntax import Syntax
from rich.tree import Tree
from rich.columns import Columns
from rich.text import Text
from rich import inspect
from rich.traceback import install


# Better error messages
install(show_locals=True)

# Main Rich object
console = Console()


# ============================================================
# 1. BASIC PRINT
# ============================================================

console.rule("1. BASIC PRINT")

console.print("Hello, Rich!")
console.print("Python is powerful.")


# ============================================================
# 2. COLORS + STYLES
# ============================================================

console.rule("2. COLORS + STYLES")

console.print("[red]ERROR[/red]")
console.print("[bold green]SUCCESS[/bold green]")
console.print("[yellow]WARNING[/yellow]")
console.print("[cyan]INFORMATION[/cyan]")

console.print(
    "Important message",
    style="bold magenta"
)


# ============================================================
# 3. INPUT
# ============================================================

console.rule("3. INPUT")

name = console.input("[bold cyan]Enter your name: [/bold cyan]")

console.print(
    f"Welcome, {name}!",
    style="bold green"
)


# ============================================================
# 4. TEXT OBJECT
# ============================================================

console.rule("4. TEXT")
text = Text("Rich makes terminal applications beautiful.")

text.stylize("bold cyan")

console.print(text)


# ============================================================
# 5. PANEL
# ============================================================

console.rule("5. PANEL")

panel = Panel(
    f"Welcome {name}!\nYou are learning the Rich library.",
    title="Python Learning",
    border_style="cyan"
)

console.print(panel)


# ============================================================
# 6. TABLE
# ============================================================

console.rule("6. TABLE")

table = Table(title="Student Information")

table.add_column("Name")
table.add_column("Age")
table.add_column("Language")
table.add_column("Marks")

table.add_row("Aman", "20", "Python", "85")
table.add_row("Rahul", "21", "C++", "91")
table.add_row("Priya", "20", "Java", "88")

console.print(table)


# ============================================================
# 7. PROGRESS BAR
# ============================================================

console.rule("7. PROGRESS")

for i in track(
    range(20),
    description="Processing..."
):
    time.sleep(0.05)


# ============================================================
# 8. STATUS / LOADING
# ============================================================

console.rule("8. STATUS")

with console.status("Working..."):
    time.sleep(2)

console.print(
    "Task completed!",
    style="bold green"
)


# ============================================================
# 9. RULE / SEPARATOR
# ============================================================

console.rule("9. RULE")

console.rule("[bold blue]Another Section[/bold blue]")


# ============================================================
# 10. MARKDOWN
# ============================================================

console.rule("10. MARKDOWN")

markdown_text = """
# Python

Python is a **high-level programming language**.

### Important Features

- Easy syntax
- Huge ecosystem
- Object-oriented
- Used in AI and web development
"""

console.print(
    Markdown(markdown_text)
)


# ============================================================
# 11. SYNTAX HIGHLIGHTING
# ============================================================

console.rule("11. SYNTAX HIGHLIGHTING")

code = '''
def greet(name):
    print(f"Hello {name}")

greet("Aman")
'''

syntax = Syntax(
    code,
    "python",
    line_numbers=True
)

console.print(syntax)


# ============================================================
# 12. JSON DISPLAY
# ============================================================

console.rule("12. JSON")

json_data = """
{
    "name": "Aman",
    "age": 20,
    "skills": ["Python", "C++", "JavaScript"]
}
"""

console.print_json(data=json_data)


# ============================================================
# 13. TREE
# ============================================================

console.rule("13. TREE")

tree = Tree("Python")

basics = tree.add("Basics")
basics.add("Variables")
basics.add("Loops")
basics.add("Functions")

advanced = tree.add("Advanced")
advanced.add("OOP")
advanced.add("Decorators")
advanced.add("Generators")

console.print(tree)


# ============================================================
# 14. COLUMNS
# ============================================================

console.rule("14. COLUMNS")

items = [
    "Python",
    "C++",
    "JavaScript",
    "React",
    "Node.js",
    "MongoDB"
]

columns = Columns(items)

console.print(columns)


# ============================================================
# 15. INSPECT
# ============================================================

console.rule("15. INSPECT")

numbers = [10, 20, 30]

inspect(numbers, methods=True)


# ============================================================
# 16. BETTER TRACEBACK
# ============================================================

console.rule("16. TRACEBACK")

try:
    result = 10 / 0

except ZeroDivisionError:
    console.print(
        "[bold red]Division by zero detected![/bold red]"
    )


# ============================================================
# FINAL MESSAGE
# ============================================================

console.print(
    Panel(
        "[bold green]RICH SHOWCASE COMPLETED[/bold green]\n\n"
        "You have now seen the major building blocks of Rich.",
        title="Finished"
    )
)