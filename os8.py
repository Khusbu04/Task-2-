# Solution: Fun Challenge - File Cleanup Bot
import os
import datetime
import shutil
def file_cleanup_bot(directory, days_old):
    if not so.path.exists(directory):
        print(f"Error: The directory '{directory}' does not exists.")
        return
    # Calculate the cutoff time
    now = datetime.datetime.now()
    cutoff_time = now - datetime.timedelta(days = days_old)
    left...........