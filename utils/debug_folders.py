# debug_folders.py
import os

target_dir = "./data/pro-git-book"

print(f"1. Checking if path exists: {os.path.exists(target_dir)}")
print(f"2. Absolute Path: {os.path.abspath(target_dir)}")

if os.path.exists(target_dir):
    print("\n3. Walking through directory structure:")
    count = 0
    for root, dirs, files in os.walk(target_dir):
        print(f"\n📂 Current Folder: {root}")
        print(f"   Subfolders found: {dirs}")
        print(f"   Files found (showing up to 5): {files[:5]}")
        count += len(files)
    print(f"\nTotal files discovered anywhere in this tree: {count}")
else:
    print("\n📂 Current Working Directory files:")
    print(os.listdir("."))