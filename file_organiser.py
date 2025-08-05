import os
import shutil

current_dir = os.getcwd()
reports_dir = os.path.join(current_dir, "reports")

if not os.path.exists(reports_dir):
    os.mkdir(reports_dir)

found_txt = False

for filename in os.listdir(current_dir):
    file_path = os.path.join(current_dir, filename)
    if os.path.isfile(file_path) and filename.endswith('.txt'):
        print(filename)
        shutil.move(file_path, os.path.join(reports_dir, filename))
        found_txt = True

if not found_txt:
    print("No .txt files found.")