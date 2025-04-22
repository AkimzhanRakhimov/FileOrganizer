import os
import shutil
from pathlib import Path

# File type defenition
def get_file_type(file):
    if file.suffix in ['.jpg', '.jpeg', '.png', '.gif']:
        return 'Images'
    elif file.suffix in ['.pdf']:
        return 'PDFs'
    elif file.suffix in ['.txt', '.docx', '.xlsx']:
        return 'Documents'
    elif file.suffix in ['.mp4', '.mkv', '.avi']:
        return 'Videos'
    else:
        return 'Others'

# Flie organization function 
def organize_files(source_folder):
    source_folder = Path(source_folder)

    # Create folders for each type
    for folder in ['Images', 'PDFs', 'Documents', 'Videos', 'Others']:
        (source_folder / folder).mkdir(exist_ok=True)

    # Checking each file in a folder 
    for file in source_folder.iterdir():
        if file.is_file():
            file_type = get_file_type(file)
            destination = source_folder / file_type / file.name
            shutil.move(file, destination)

# Function calling
organize_files('')  # Type your path to folder
