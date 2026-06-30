import os
import shutil

def move_jpg_files():
    base_dir = os.getcwd()
    source_folder = os.path.join(base_dir, "pic1")
    destination_folder = os.path.join(base_dir, "pic2")

    if not os.path.exists(source_folder):
        print(f"Error: Source folder '{source_folder}' not found.")
        print("Please create a 'pic1' folder in this directory and add some images first.")
        return

    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
        print(f"Created destination folder: {destination_folder}")

    files_moved = 0
    for filename in os.listdir(source_folder):
        if filename.lower().endswith((".jpg", ".jpeg")):
            source_path = os.path.join(source_folder, filename)
            dest_path = os.path.join(destination_folder, filename)
            
            shutil.move(source_path, dest_path)
            print(f"Moved: {filename}")
            files_moved += 1
            
    print(f"\nTask Complete. Total files moved: {files_moved}")

if __name__ == "__main__":
    move_jpg_files()