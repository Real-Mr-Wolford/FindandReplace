

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


