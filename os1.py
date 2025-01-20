import os
import shutil
# Create a new directory
if not os.path.isdir("test_directory"):
    os.mkdir("test_directory")
# Change the current working directory to the new directory
os.chdir("test_directory")
print("Current working directory:", os.getcwd())
# Create a text file in the directory
with open("example.txt", "w") as file:
    file.write("This is a test file.")
# List files in the current directory
print("Files in directory:", os.listdir())
# Copy the file
shutil.copy("example.txt", "copy_example.txt")
# Move the copied file tp a new location(renaming it in process)
shutil.move("copy_example.txt", "../moved_example.txt")
# Go back to the parent directory
os.chdir("..")
# Remove the test directory and its contents
shutil.rmtree("test_directory")
os.remove("moved_example.txt") #remove the moved file
print("Cleanup complete")