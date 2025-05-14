import os
import shutil

source_folder = "/path/to/your/source/folder"
destination_folder = "/path/to/your/destination/folder"

if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

for filename in os.listdir(source_folder):
    if filename.endswith(".txt"):
        source_path = os.path.join(source_folder, filename)
        destination_path = os.path.join(destination_folder, filename)
        shutil.move(source_path, destination_path)
        print(f"Moved: {filename} to {destination_folder}")

print("File moving complete.")