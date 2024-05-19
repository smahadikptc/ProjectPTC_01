import os
import shutil
import zipfile


class FolderManager:
    def __init__(self):
        # Define paths
        self.python_folder_path = "C:\\python"
        self.s2o_folder_path = os.path.join(self.python_folder_path, "s2o")
        self.s2o_zip_path = os.path.join(self.python_folder_path, "s2o.zip")

    def delete_s2o_folder(self):
        # Check if the s2o folder exists and delete it
        if os.path.exists(self.s2o_folder_path):
            shutil.rmtree(self.s2o_folder_path)
            print("Deleted existing 's2o' folder.")

    def extract_zip_file(self):
        # Extract the zip file directly into the python folder
        with zipfile.ZipFile(self.s2o_zip_path, 'r') as zip_ref:
            zip_ref.extractall(self.python_folder_path)
        print("Extracted 's2o.zip' into 'python' folder.")

    def main(self):
        self.delete_s2o_folder()
        self.extract_zip_file()


if __name__ == "__main__":
    folder_manager = FolderManager()
    folder_manager.main()
