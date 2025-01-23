# Solution: Fun Challenge - File Cleanup Bot
import os
import datetime
import shutil
def file_cleanup_bot(directory, days_old):
    if not os.path.exists(directory):
        print(f"Error: The directory '{directory}' does not exists.")
        return
    # Calculate the cutoff time
    now = datetime.datetime.now()
    cutoff_time = now - datetime.timedelta(days = days_old)
    # Create an 'Archive' directory
    archive_dir = os.path.join(directory, "Archive")
    os.makedirs(archive_dir, exist_ok = True)
    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)
        # Skip directories
        if os.path.isdir(file_path):
            continue
        # Check file's modification time
        file_mtime = datatime.datetime.fromtimestamp(os.path.getmtime(file_path))
        if file_mtime < cutoff_time:
            shutil.move(file_path, os.path.join(archive_dir, file_name))
            print(f"Moved '{file_name}' to Archive")
    # Ask user for confirmation before deleting the archive folder
    confirm = input(f"Do you want to delete the 'Archive' folder? (yes/no): ").strip().lower()
    if confirm == 'yes':
        shutil.rmtree(archive_dir)
        print("Archive folder deleted.")
# Example usage
file_cleanup_bot("./example_directory", 1)