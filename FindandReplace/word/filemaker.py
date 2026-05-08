from pathlib import Path
import textwrap
import os
import csv


def writeFiles():
    nam = input("Enter the base name for the files: ")
    csv_file = input("Currently, this configuration allows for three part letters.\n A name, header 0; the body of text,  header 1; and a signature, header 2.\nEnter the path to your data (.csv): ")

    directory = getDirectory()

    wrap_width = 70
    if not os.path.exists(directory):
        os.makedirs(directory)
    with open(csv_file, mode="r", encoding="utf-8") as c:
        reader = csv.DictReader(c)
        headers = reader.fieldnames #list of column names
        for i, row in enumerate(reader):
            file_path = directory / f"{nam}_{i}.txt"
            unwrapped_message = row[headers[1]]
            wrapped_message = textwrap.fill(unwrapped_message, width=wrap_width)
            with open(file_path, "w") as f: 
                #You can add or change the stuff written to the files here
                f.write(f"Dear {row[headers[0]]}\n\n")
                f.write(f"{wrapped_message}\n\n")
                f.write(f"{row[headers[2]]}")
                #f.write(f"This is file {i}")
                #f.write("[SIGNATURE]")
                #f.write("\n")
                #f.write("[DATE]")
def makeNewFiles():
    writeFiles()
def getDirectory():
    directory = Path(input("Enter the directory path: "))
    return directory
