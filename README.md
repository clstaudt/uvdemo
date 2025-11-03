# uvdemo

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
uv add uvdemo
```

## Development with uvdemo-workbench

For interactive development with notebooks, use the companion workbench:

```bash
# Clone both repositories side-by-side
parent-directory/
├── uvdemo/
└── uvdemo-workbench/

# Setup the workbench (it will use uvdemo as editable dependency)
cd uvdemo-workbench
just setup
```

See [uvdemo-workbench](../uvdemo-workbench/README.md) for details.

## Library Functions

- `output_greeting()` - Display a styled greeting in a panel
- `output_table()` - Display a formatted table
- `work_work()` - Show a spinner animation

