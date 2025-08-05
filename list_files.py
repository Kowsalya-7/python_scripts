import os

current_dir = os.getcwd()
found_txt = False

for filename in os.listdir(current_dir):
    if os.path.isfile(os.path.join(current_dir, filename)) and filename.endswith('.txt'):
        print(filename)
        found_txt = True

if not found_txt:
    print("No .txt files found.")
