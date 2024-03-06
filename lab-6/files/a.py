import os
import shutil

#1
def list_dir_files(path):
    dirs = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    return {"directories": dirs, "files": files}

#2
def check_access(path):
    return {
        "exists": os.path.exists(path),
        "readable": os.access(path, os.R_OK),
        "writable": os.access(path, os.W_OK),
        "executable": os.access(path, os.X_OK)
    }

#3
def test_path(path):
    if os.path.exists(path):
        return {
            "exists": True,
            "filename": os.path.basename(path),
            "directory": os.path.dirname(path)
        }
    else:
        return {"exists": False}

#4
def count_lines(file_path):
    with open(file_path, 'r') as file:
        return sum(1 for line in file)

#5
def write_list_to_file(file_path, lst):
    with open(file_path, 'w') as file:
        for item in lst:
            file.write(f"{item}\n")

#6
def generate_text_files():
    for i in range(26):
        with open(f"{chr(65 + i)}.txt", 'w') as file:
            file.write(f"This is file {chr(65 + i)}")

#7
def copy_file(source, destination):
    shutil.copy(source, destination)

#8
def delete_file(path):
    if os.path.exists(path) and os.access(path, os.W_OK):
        os.remove(path)
        return True
    else:
        return False

example_path = "/mnt/data"  
example_file_path = "/mnt/data/test.txt"

generate_text_files()