import os
import shutil
# Define the directory to organize
directory = "./example_directory"
# Create the directory and some test files
os.makedirs(directory, exist_ok = True)
with open(os.path.join(directory, "file1.txt"), "w") as f:
    f.write("Text file content")
with open(os.path.join(directory, "file2.jpg"), "w") as f:
    f.write("Image file content")
with open(os.path.join(directory, "file3.mp3"), "w") as f:
    f.write("Audio file content")
# Function to organize files by type
def organize_files_by_type(directory):
    # Get a list of all files in the directory
    for file_name in os.listdir(directory):
        file_path = os. path.join(directory, file_name)
        # Skip directories
        if os.path.isdir(file_path):
            continue
        # Get the file extension
        file_extension = file_name.split(".")[-1]
        # Create a folder for the file type if it doesn't exist
        type_folder = os.path.join(directory, file_extension)
        os.makedirs(type_folder, exist_ok = True)
        # Move the file to the appropriate folder
        shutil.move(file_path, os.path.join(type_folder, file_name))
        print(f"Moved {file_name} to {type_folder}/")
# Call the function
organize_files_by_type(directory)
# Display organized structure
for root, dirs, files in os.walk(directory):
    print(f"\nIn {root}:")
    for dir_name in dirs:
        print(f" Directory: {dir_name}")
    for file_name in files:
        print(f" File: {file_name}")
# Clean up
# shutil.rmtree(directory)