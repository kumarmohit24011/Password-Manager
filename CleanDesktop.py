import os
import shutil

# Set your Desktop path
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

# File type folders
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".svg"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx", ".xlsx"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".7z"],
    "Scripts": [".py", ".js", ".html", ".css"],
    "Others": []
}

def clean_desktop():
    for file_name in os.listdir(desktop_path):
        file_path = os.path.join(desktop_path,file_name)

        if os.path.isdir(file_path):
            continue

        moved =False
        for folder,extensions in file_types.items():
            if any(file_name.lower().endswith(ext) for ext in extensions):
                folder_path =os.path.join(desktop_path,folder)
                os.makedirs(folder_path,exist_ok=True)
                shutil.move(file_path,os.path.join(folder_path,file_name))
                moved=True
                break
        if not moved :
            other_path  =os.path.join(desktop_path,"others")
            os.makedirs(other_path,exist_ok=True)
            shutil.move(file_path,os.path.join(other_path,file_name))
    print("Desktop Cleaned successfully !")
clean_desktop()