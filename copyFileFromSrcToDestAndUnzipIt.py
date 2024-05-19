import os
import shutil
import zipfile


def delete_all_files_and_folders(folder_path):
    """Delete all files and folders in the specified folder."""
    for root, dirs, files in os.walk(folder_path, topdown=False):
        for file in files:
            file_path = os.path.join(root, file)
            os.remove(file_path)
            print(f"Deleted file: {file_path}")
        for dir1 in dirs:
            dir_path = os.path.join(root, dir1)
            shutil.rmtree(dir_path)
            print(f"Deleted folder: {dir_path}")


# Flag to track whether initial cleanup has been done
cleanup_done = False


def clean_destination_folder(dest_folder):
    global cleanup_done
    if not cleanup_done:
        delete_all_files_and_folders(dest_folder)
        cleanup_done = True


def copy_and_extract_zip(src_folder, dest_folder):
    """Copy the zip folder from source to destination and extract it."""
    zip_files = [f for f in os.listdir(src_folder) if f.endswith('.zip')]
    if not zip_files:
        print(f"No zip files found in source folder: {src_folder}")
        return

    zip_file = os.path.join(src_folder, zip_files[0])

    shutil.copy(zip_file, dest_folder)
    print(f"Copied zip file '{os.path.basename(zip_file)}' to destination folder: {dest_folder}")

    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(dest_folder)
    print(f"Extracted contents of zip file in destination folder: {dest_folder}")

    os.remove(os.path.join(dest_folder, os.path.basename(zip_file)))
    print(f"Removed zip file '{os.path.basename(zip_file)}' from destination folder: {dest_folder}")


# Example usage:
folder_to_clean = "C:\\dest"
source_folder = "C:\\src"
destination_folder = "C:\\dest"

# Step 1: Delete all files and folders in the destination folder initially
clean_destination_folder(folder_to_clean)

# Step 2: Copy and extract the zip folder from source to destination
copy_and_extract_zip(source_folder, destination_folder)
