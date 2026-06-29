from pathlib import Path


def list_files(folder_path):
    path = Path(folder_path)

    if not path.exists():
        print("Folder does not exist.")
        return

    if not path.is_dir():
        print("This path is not a folder.")
        return

    print("\nFiles found:\n")

    for item in path.iterdir():
        if item.is_file():
            print(item.name)


def main():
    print("File Organizer")
    print("-" * 30)

    folder = input("Enter folder path: ")

    list_files(folder)


if __name__ == "__main__":
    main()