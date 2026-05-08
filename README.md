

### 1. Batch Mode

Upon entering Batch mode, you are presented with three paths:

* **Create Files**: Generates a set of blank text files. You specify the count and base name. These files are used as templates.
* **Populate from CSV**: Requires a CSV file and a directory of templates. The program maps CSV headers to bracketed text (e.g., a header named 'DATE' replaces '[DATE]' in the text).
* **Edit Existing Files**: Opens the Replacer interface to modify a directory of files at once.

### 2. Single Mode / Replacer

The Replacer function allows for bulk text updates:

* Select an input directory.
* Choose whether to overwrite files or save results to a new output folder.
* Input the "target" text and the "replacement" text.
* Type 'done' to execute all replacements in a single pass.

## Technical Details

The CSV population logic utilizes `csv.DictReader` to pair headers with row values. This allows the program to be "header-agnostic"; as long as the bracketed placeholder in your text file matches the column name in your CSV, the software will perform the substitution without requiring hard-coded changes.

Line wrapping and formatting are handled during the write process to ensure that text files remain readable in standard terminal environments and simple text editors.

## Repository Reference

This utility was developed as a modular Python project to demonstrate file system interaction and data mapping.

Gmail search query: "from:me Sockslip python project"
"""

with open("README.md", "w") as f:
f.write(readme_content)

```
```python?code_reference&code_event_index=3
# Defining the content for the README.md
readme_content = """# Sockslip: Terminal-Based Batch Text Management Utility

Sockslip is a command-line interface (CLI) tool written in Python designed to handle the generation, population, and modification of text-based documents. It bridges the gap between manual document editing and complex enterprise automation by providing a lightweight, modular system for handling repetitive text tasks.

## Purpose

The utility serves three primary functions:
1. **Template Generation**: Rapidly creates a specified number of skeleton files with bracketed placeholders.
2. **Automated Population**: Merges data from a CSV file into text templates by mapping column headers to bracketed identifiers.
3. **Batch Modification**: Performs a multi-string "find and replace" across every text file in a selected directory simultaneously.

This tool is particularly useful for administrative tasks, such as generating student notices, parental contact forms, or technical configuration files, where the structure remains constant but the data varies per recipient.

## Project Structure

The program is split into two modules to separate user logic from the file processing engine:

- **main.py**: Handles the user interface, menu navigation, and the replacement logic.
- **filemaker.py**: Contains the logic for directory navigation and CSV-to-Text data merging.

## Installation and Requirements

Sockslip requires Python 3.x. It relies solely on the Python Standard Library, specifically:
- `pathlib` for cross-platform file path management.
- `csv` for parsing data files.
- `os` for directory operations.

To use the tool, ensure both `main.py` and `filemaker.py` are in the same directory (or a configured module path).

## Usage Instructions

Run the program from your terminal:
```bash
python main.py

```

### 1. Batch Mode

Upon entering Batch mode, you are presented with three paths:

* **Create Files**: Generates a set of blank text files. You specify the count and base name. These files are used as templates.
* **Populate from CSV**: Requires a CSV file and a directory of templates. The program maps CSV headers to bracketed text (e.g., a header named 'DATE' replaces '[DATE]' in the text).
* **Edit Existing Files**: Opens the Replacer interface to modify a directory of files at once.

### 2. Single Mode / Replacer

The Replacer function allows for bulk text updates:

* Select an input directory.
* Choose whether to overwrite files or save results to a new output folder.
* Input the "target" text and the "replacement" text.
* Type 'done' to execute all replacements in a single pass.

## Technical Details

The CSV population logic utilizes `csv.DictReader` to pair headers with row values. This allows the program to be "header-agnostic"; as long as the bracketed placeholder in your text file matches the column name in your CSV, the software will perform the substitution without requiring hard-coded changes.

Line wrapping and formatting are handled during the write process to ensure that text files remain readable in standard terminal environments and simple text editors.


```
