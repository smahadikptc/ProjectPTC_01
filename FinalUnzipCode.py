import os
import shutil
import zipfile


class FolderManager:
    def __init__(self):
        # Define paths
        self.python_folder_path = "C:\\python"
        self.s2o_folder_path = os.path.join(self.python_folder_path, "s2o")
        self.s2o_zip_path = os.path.join(self.python_folder_path, "s2o.zip")

    def delete_and_create_folders(self):
        # Check if the s2o folder exists and delete it
        if os.path.exists(self.s2o_folder_path):
            shutil.rmtree(self.s2o_folder_path)
            print("Deleted existing 's2o' folder.")

        # Recreate the s2o folder
        os.makedirs(self.s2o_folder_path)
        print("Created new 's2o' folder.")

    def copy_and_extract_zip_file(self):
        # Copy s2o.zip into s2o folder
        shutil.copy(self.s2o_zip_path, self.s2o_folder_path)
        print("Copied 's2o.zip' into 's2o' folder.")

        # Extract the zip file
        with zipfile.ZipFile(os.path.join(self.s2o_folder_path, "s2o.zip"), 'r') as zip_ref:
            zip_ref.extractall(self.s2o_folder_path)
        print("Extracted 's2o.zip' to 's2o' folder.")

    def main(self):
        self.delete_and_create_folders()
        self.copy_and_extract_zip_file()


if __name__ == "__main__":
    folder_manager = FolderManager()
    folder_manager.main()
