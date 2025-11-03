# uvdemo

**Demo repository** showcasing a production library setup with uv.

This is a sample Python library providing Rich-based console output utilities, designed to demonstrate best practices for structuring a production package with uv.

## Standalone Usage

Install and use as a regular Python package:

```bash
# Install dependencies
uv sync

# Run the demo
uv run python main.py
```

Or install in another project:

```bash
uv add uvdemo
```

## Dev Container Support

This repository includes a minimal devcontainer configuration for library development:

- Open in VS Code with Dev Containers extension
- Container automatically runs `uv sync` on creation
- Includes Python, Pylance, and Ruff extensions
- Based on official `python:3.12-slim` image with uv installed

## Development with uvdemo-workbench

This repository demonstrates the **production repo + workbench repo pattern** with uv. For interactive development with notebooks and scripts, use the companion workbench repository:

```bash
# Clone both repositories side-by-side
parent-directory/
├── uvdemo/           # Production library (this repo)
└── uvdemo-workbench/ # Development workbench

# Setup the workbench (it will use uvdemo as editable dependency)
cd uvdemo-workbench
just setup
```

The workbench imports this library as an editable dependency, allowing you to test changes in real-time without reinstalling. See [uvdemo-workbench](../uvdemo-workbench/README.md) for details.

## Library Functions

- `output_greeting()` - Display a styled greeting in a panel
- `output_table()` - Display a formatted table
- `work_work()` - Show a spinner animation

