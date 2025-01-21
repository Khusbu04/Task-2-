import datetime
import os
import shutil
def create_backup(source_directory):
    if not os.path.exists(source_directory):
        print(f"Error: The directory '{source_directory}' does not exists.")
        return
    # Generate a time tamped backup name
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_name = f"backup_{timestamp}"
    # Create a zip archive of the source directory
    shutil.make_archive(backup_name, 'zip', source_directory)
    print(f"Backup created: {backup_name}.zip")
# Example usage
create_backup("./example_directory")