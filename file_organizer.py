import os
import shutil

def organize_files_in_folder(folder_path, selected_extensions, label_map):
    moved_files = {}
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        if os.path.isfile(file_path):
            _, ext = os.path.splitext(file)
            ext = ext.lower()
            if ext in selected_extensions:
                target_dir = os.path.join(folder_path, label_map[ext])
                os.makedirs(target_dir, exist_ok=True)
                shutil.move(file_path, os.path.join(target_dir, file))
                moved_files.setdefault(label_map[ext], 0)
                moved_files[label_map[ext]] += 1
    return moved_files
