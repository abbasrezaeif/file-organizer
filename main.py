from pathlib import Path
import shutil


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


def get_file_moves(folder_path):
    path = Path(folder_path)

    moves = []

    for item in path.iterdir():
        if item.is_file():
            extension = get_file_extension(item)
            category = get_category(extension)
            destination = path / category / item.name

            moves.append((item, destination))

    return moves


def organize_files(folder_path):
    path = Path(folder_path)

    if not path.exists():
        print("Folder does not exist.")
        return

    if not path.is_dir():
        print("This path is not a folder.")
        return

    create_category_folders(path)

    moves = get_file_moves(path)

    if not moves:
        print("No files found.")
        return

    print("\nPreview:\n")

    for source, destination in moves:
        print(f"{source.name}")
        print(f"  -> {destination}")
        print()

    print(f"Total files: {len(moves)}")

    confirm = input("\nMove these files? (y/n): ").strip().lower()

    if confirm != "y":
        print("Operation cancelled.")
        return

    for source, destination in moves:
        shutil.move(str(source), str(destination))

    print("\nFiles organized successfully.")


def main():
    print("File Organizer")
    print("-" * 30)

    folder = input("Enter folder path: ")

    organize_files(folder)


if __name__ == "__main__":
    main()