from Zipper import Zipper
from pathlib import Path

def main():
    print("Welcome to Zipper, the tool for compressing files into multiple formats!\n")
    
    print("Let's get started. First, select a type of compression. Accepted types are: zip, tar, gtar and btar.")
    extensions = ("zip", "tar", "gtar", "btar")

    extension = input("Select a extension: ")

    while extension not in extensions:
        print(f"Sorry, but that's not a valid extension, the valid one are {extensions}\n")
        extension = input("Select a extension: ")

    print(f"\nOk, perfect, so you choose {extension}. Good choise!\n")
    print("What do you want to compress?. Type the relative path to the folder using /\n")
    print("Example: /my_folder/folder_to_compress\n")
    
    input_folder = Path(input("Enter your folder: "))

    while input_folder.exists() is False:
        print("\nPlease, select a valid path!\n")
        input_folder = Path(input("Enter your folder: "))

    print(f"\nOk, we'll compress {input_folder}\n")

    print("What is your compressed file be named?\n")
    
    output_name = input("Enter a name: ")

    print(f"This we'll create the following file: {output_name}.{extension}\n")

    options = ("Y","N")

    confirm = input("Do you want to proceed?: [Y]es [N]o")

    while confirm not in options:
        print("\nSorry, but that'a not a valid option!\n")
        confirm = input("Do you want to proceed?: [Y]es [N]o: ")

    if confirm == "N":
        print("\nAborting proccess, bye!")
        return
    else:
        print("\nCompressing...\n")
        compresser = Zipper(input_folder, output_name, extension)
        compresser.compressFolder()
        print("Succesfully created the file!")
        return

if __name__ == "__main__":
    main()