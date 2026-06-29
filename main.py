from pathlib import Path


FILE_CATEGORIES = {
    "PDF": [".pdf"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Music": [".mp3", ".wav", ".aac"],
    "Documents": [".doc", ".docx", ".txt", ".rtf"],
    "Spreadsheets": [".xls", ".xlsx", ".csv"],
    "Archives": [".zip", ".rar", ".7z"],
}


def get_file_extension(file_path):
    return file_path.suffix.lower()


def get_category(extension):
    for category, extensions in FILE_CATEGORIES.items():
        if extension in extensions:
            return category

    return "Others"


def create_category_folders(base_path):
    folders = list(FILE_CATEGORIES.keys()) + ["Others"]

    for folder in folders:
        folder_path = base_path / folder
        folder_path.mkdir(exist_ok=True)


def list_files(folder_path):
    path = Path(folder_path)

    if not path.exists():
        print("Folder does not exist.")
        return

    if not path.is_dir():
        print("This path is not a folder.")
        return

    create_category_folders(path)

    print("\nFiles found:\n")

    count = 0

    for item in path.iterdir():
        if item.is_file():
            count += 1
            extension = get_file_extension(item)

            if extension == "":
                extension = "No Extension"

            category = get_category(extension)
            print(f"{item.name}  -->  {extension}  -->  {category}")

    print(f"\nTotal files: {count}")


def main():
    print("File Organizer")
    print("-" * 30)

    folder = input("Enter folder path: ")

    list_files(folder)


if __name__ == "__main__":
    main()