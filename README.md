### 📂 File Organizer Script

#### 📝 Description
This is a Python script that organizes files in a specified directory into folders based on their type. It sorts files into categories like:
- **Images**
- **PDFs**
- **Documents**
- **Videos**
- **Others**

---

#### ⚙️ Technologies Used
- **Python 3**  
- **os** (file handling)  
- **shutil** (file moving)  
- **pathlib** (path management)

---

#### 📊 Features
- Automatically sorts files based on file extensions.
- Creates directories for each type if they don't already exist.
- Moves files to corresponding directories (Images, PDFs, Documents, Videos, Others).

---

#### 🚀 How to Run

1. Clone the repository:
```bash
git clone https://github.com/yourusername/file-organizer.git
cd file-organizer
```

2. Modify the script to point to the folder you want to organize.
```python
organize_files('path_to_your_folder')  # Specify your folder path
```

3. Run the script:
```bash
python organize_files.py
```

---

#### 📌 Notes
- The script is designed to work on files in a local folder.
- You can add more file types to the `get_file_type` function based on your needs.

---
