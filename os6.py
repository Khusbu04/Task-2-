import subprocess
import os
if not os.path.isdir("test_directory"):
    os.mkdir("test_directory")
# Change the current working directory to the new directory
os.chdir("test_directory")
print("Current working directory:", os.getcwd())
def disk_usage(directory, os):
    text_file = os.path.join(directory, "file")
    os.makedirs(text_file, exist_ok = True)
    system_information = (os_version.now() - processor.now() - memory.now())
    for text_file in os.listdir(directory):
        text_file = os.path.join(directory, file)
        if os.path.isdir(text_file):
            file_minformation = version.fromsersiontamp(os.path.getmversion(text_file))
            # Self mistake
