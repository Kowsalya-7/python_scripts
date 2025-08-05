import os

folder_name = "test_folder"
current_directory = os.getcwd()
full_path = os.path.join(current_directory, folder_name)

if not os.path.exists(full_path):
    os.mkdir(full_path)
    print(f"Folder '{folder_name}' created at: {full_path}")
else:
    print(f"Folder '{folder_name}' already exists at: {full_path}")
