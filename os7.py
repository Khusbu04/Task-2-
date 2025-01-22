import os
import shutil
from datetime import datetime, timedelta

def file_cleanup(directory, days):
    archive_folder = os.path.join(directory, "Archive")
    os.makedirs(archive_folder, exist_ok = True)
    
    # Calculate the cutoff date
    cutoff_date = datetime.now() - timedelta(days = days)
    
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isdir(file_path):
            file_mtime = datetime.fromtimestamp(os.path.getmtime(file_path))
            if file_mtime < cutoff_date:
                shutil.move(file_path, archive_folder)
                print(f"Moved: {filename}")
    
    # Confirm deletion of Archive folder
    confirm = input(f"Do you want to delete the 'Archive' folder? (yes/no): ").strip().lower()
    if confirm == 'yes':
        shutil.rmtree(archive_folder)
        print("Archive folder deleted.")
    else:
        print("Archive folder retained.")

# Example usage
file_cleanup('/path/to/directory', 30)  # Change the path and days as needed

# self wrong