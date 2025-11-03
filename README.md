# uvtest

A library providing Rich-based console output utilities.

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
uv add uvtest
```

## Development with uvtest-workbench

For interactive development with notebooks, use the companion workbench:

```bash
# Clone both repositories side-by-side
parent-directory/
├── uvtest/
└── uvtest-workbench/

# Setup the workbench (it will use uvtest as editable dependency)
cd uvtest-workbench
just setup
```

See [uvtest-workbench](../uvtest-workbench/README.md) for details.

## Library Functions

- `output_greeting()` - Display a styled greeting in a panel
- `output_table()` - Display a formatted table
- `work_work()` - Show a spinner animation

