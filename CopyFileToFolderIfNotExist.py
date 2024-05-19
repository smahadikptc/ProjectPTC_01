import os
import shutil

def paste_file_if_empty(src_file, dest_folder):
    # Check if the destination folder is empty
    if not os.listdir(dest_folder):
        # Copy the file to the destination folder
        shutil.copy(src_file, dest_folder)
        print(f"File '{os.path.basename(src_file)}' copied to '{dest_folder}'")
    else:
        # If the folder is not empty, delete all files in the folder
        for filename in os.listdir(dest_folder):
            file_path = os.path.join(dest_folder, filename)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
                    print(f"File '{filename}' deleted from '{dest_folder}'")
            except Exception as e:
                print(f"Error while deleting file '{filename}': {e}")

        # Copy the file to the destination folder
        shutil.copy(src_file, dest_folder)
        print(f"File '{os.path.basename(src_file)}' copied to '{dest_folder}'")


# Example usage:
source_file = "c:\\Src\\Hello.txt"
destination_folder = "C:\\dest"

# Call the function
paste_file_if_empty(source_file,destination_folder)