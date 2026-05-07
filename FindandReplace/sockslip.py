
from word import filemaker
import os

def single():
    replacer()

def batch():
    need = input("Do you need to create files? Y/n")
    if need.lower() == "y":
        filemaker.createFiles()
    else:
        print("Skipping file creation.")

    
    replacer()
def replacer():
    replacements = {}
    print("Text Replacer")
    directory = filemaker.getDirectory()
    input_folder = directory
    output_folder = ""
    dir_branch = input("Is the input folder the same as the output folder? Y/n: ")
    if dir_branch.lower() == 'n':
        output_folder = input("Enter the output folder path: ")
    else:
        output_folder = input_folder
    print("Enter the words you wish to replace")
    print("When finshed, type 'done'\n")

    while True:
        target = input("Find this text: ").strip()
        if target.lower() == 'done':
            break
        replacement = input(f"Replace '{target}' with: ").strip()
        replacements[target] = replacement
        print("Added\n")

    #input_folder = directory
    #output_folder = directory

    for folder in [input_folder,output_folder]:
        if not os.path.exists(folder):
            os.makedirs(folder)
             

    files = os.listdir(input_folder)
    text_files = [f for f in files if f.endswith(".txt")]

    if not text_files:
        print(f"\nNo .txt files found in {input_folder}")
        print("Please put some files in that folder and run again!")
    else:
        print(f"\nFound {len(text_files)} .txt file(s) in {input_folder}")
        print("Processing")

        for filename in text_files:
            input_path = os.path.join(input_folder,filename)
            with open(input_path,"r", encoding="utf-8") as f:
                content = f.read()

            for target, replacement in replacements.items():
                content = content.replace(target, replacement)

            output_path = os.path.join(output_folder, filename)
            with open(output_path,"w",encoding = "utf-8") as f:
                f.write(content)
            print(f"Processed {filename}")

        print("All files processed.")


r_Type = input("Do you want to do a <batch> edit or a <single> file?")
if(r_Type == "single"):
    single()
elif r_Type == "batch":
    batch()
else:
    print("Invalid input. Please enter 'single' or 'batch'.")
