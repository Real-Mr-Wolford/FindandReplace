from pathlib import Path
import os
def createFiles():
    num = int(input("Enter the number of files to create: "))
    nam = input("Enter the base name for the files: ")
    directory = getDirectory()
    if not os.path.exists(directory):
        os.makedirs(directory)
    for i in range(num):
        file_path = directory / f"{nam}_{i}.txt"
        with open(file_path, "w") as f: 
            #You can add or change the stuff written to the files here
            f.write(f"This is file {i}")
            f.write("[SIGNATURE]")
            f.write("\n")
            f.write("[DATE]")
def getDirectory():
    directory = Path(input("Enter the directory path: "))
    return directory