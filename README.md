# 📁 File Organizer & Batch Renamer

A Python application that automatically organizes files into folders based on their file types.

---

## ✨ Features

- 📂 Organize files by category
- 🖼️ Detect images, PDFs, videos, documents, archives, music, spreadsheets and more
- 👀 Preview file movements before executing
- ✅ Confirmation before moving files
- 📦 Automatically creates category folders
- 🐍 Built with Python and pathlib

---

## 📂 Categories

- PDF
- Images
- Videos
- Music
- Documents
- Spreadsheets
- Archives
- Others

---

## 🚀 Example

Before:

Downloads/

```
resume.pdf
photo.jpg
movie.mp4
notes.txt
```

After:

Downloads/

```
PDF/
    resume.pdf

Images/
    photo.jpg

Videos/
    movie.mp4

Documents/
    notes.txt
```

---

## 💻 Installation

```bash
git clone https://github.com/abbasrezaeif/file-organizer.git

cd file-organizer

python -m venv .venv

source .venv/bin/activate

python main.py
```

---

## 🛠 Technologies

- Python 3
- pathlib
- shutil

---

## 📌 Future Improvements

- GUI version
- Drag & Drop support
- Batch Rename
- Undo feature
- Logging
- Configuration file

---

## 👨‍💻 Author

Abbas Rezaei