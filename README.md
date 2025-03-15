# Python UV Starter

A simple Python project using UV for package management.

## About UV

UV (pronounced "ultraviolet") is a fast Python package installer and resolver, designed as a modern alternative to pip. UV is built in Rust and offers significantly faster package installation and resolution compared to traditional tools.

## Setup

1. Install UV:
```bash
pip install uv
```

2. Create a virtual environment and install dependencies:
```bash
# Create and activate a virtual environment
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
uv pip install -e .
```

## Development

### Running the Application

```bash
python -m mypackage.main
```

### Running Tests

```bash
pytest
```

## Project Structure

- `src/mypackage/`: Main package code
- `tests/`: Test files
- `pyproject.toml`: Project configuration and dependencies

## License

MIT