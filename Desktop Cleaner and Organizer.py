import os
import shutil

def organize_desktop(desktop_path):
    # catagory definition 
    categories = {
        "Images": [".jpg", ".jpeg", ".png", ".gif"],
        "Documents": [".pdf", ".doc", ".docx", ".txt"],
        "Videos": [".mp4", ".avi", ".mkv", ".mov"],
        "Music": [".mp3", ".wav", ".flac"],
        "Others": []  # Default category for random stuff
    }

    # Create subfolders (cat)
    for category in categories:
        category_path = os.path.join(desktop_path, category)
        os.makedirs(category_path, exist_ok=True)

    # Organize files > subfolders
    for filename in os.listdir(desktop_path):
        file_path = os.path.join(desktop_path, filename)

        if os.path.isdir(file_path) or filename == "organize_desktop.py":
            continue

        file_extension = os.path.splitext(filename)[1].lower()
        category = "Others"  # Default category for unknown file types
        for key, extensions in categories.items():
            if file_extension in extensions:
                category = key
                break

        new_path = os.path.join(desktop_path, category, filename)
        shutil.move(file_path, new_path)
        print(f"Moved '{filename}' to '{category}' folder.")


    other_folders_path = os.path.join(desktop_path, "Other Folders")
    os.makedirs(other_folders_path, exist_ok=True)

   
    for folder_name in [f for f in os.listdir(desktop_path) if os.path.isdir(os.path.join(desktop_path, f))]:
        folder_path = os.path.join(desktop_path, folder_name)
        new_folder_path = os.path.join(other_folders_path, folder_name)
        shutil.move(folder_path, new_folder_path)
        print(f"Moved folder '{folder_name}' to 'Other Folders'.")

if __name__ == "__main__":
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    organize_desktop(desktop_path)
