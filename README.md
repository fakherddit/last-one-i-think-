# Session Title Structure

A simple Python module for managing session titles with improved clarity and structure.

## Overview

This project provides a clean and structured way to format session titles with optional components:
- **Prefix**: Category or type indicator (e.g., `[WIP]`, `[FEATURE]`, `[BUG]`)
- **Main**: The primary title text
- **Suffix**: Additional context (e.g., `(improved clarity)`, `(urgent)`)

## Usage

### Using the SessionTitle class

```python
from session_title import SessionTitle

# Create a structured title
title = SessionTitle("WIP", "Update session title structure", "improved clarity")
print(title)  # Output: [WIP] Update session title structure (improved clarity)
```

### Using the factory function

```python
from session_title import create_session_title

# Create a title with all components
title = create_session_title("FEATURE", "Add authentication", "high priority")
print(title)  # Output: [FEATURE] Add authentication (high priority)

# Create a simple title
title = create_session_title(main="Daily meeting")
print(title)  # Output: Daily meeting
```

## Running the Examples

```bash
python session_title.py
```

## Running Tests

```bash
python -m unittest test_session_title.py
```

## License

This is a demonstration project.