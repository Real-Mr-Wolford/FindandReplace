from pathlib import Path
import os
import csv
def writeFiles():
    nam = input("Enter the base name for the files: ")
    csv_file = input("Enter the path to your data (.csv): ")

    directory = getDirectory()
    if not os.path.exists(directory):
        os.makedirs(directory)
    with open(csv_file, mode="r", encoding="utf-8") as c:
        reader = csv.DictReader(c)
        headers = reader.fieldnames #list of column names
        for i, row in enumerate(reader):
            file_path = directory / f"{nam}_{i}.txt"
            with open(file_path, "w") as f: 
                #You can add or change the stuff written to the files here
                f.write(f"Dear {row[headers[0]]}\n\n")
                f.write(f"{row[headers[1]]}\n\n")
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
