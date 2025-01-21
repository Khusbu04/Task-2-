#      Question
# Process Automation with Subprocess
#Task: Automate a system-level task such as:
#Listing all running processes and saving the output to a file.
#Monitoring system resource usage (e.g., CPU and memory stats) by running appropriate system commands (top, ps, or tasklist).
#Learning Goals:
#Use subprocess.run() to execute system commands.
#Capture command output with capture_output=True.
#Write the captured output to a text file for further analysis.
import subprocess
import os
def list_running_processes(output_file):
    try:
        # Execute the system command to list processes
        command = ['tasklist'] if os.name == 'nt' else ['ps', 'aux']
        result = subprocess.run(command, capture_output = True, text = True)
        # Save the output to a file
        with open(output_file, 'w') as file:
            file.write(result.stdout)
        print(f"Process list saved to '{output_file}'")
    except Exception as e:
        print(f"Error: {e}")
# Example usade
list_running_processes("process_list.txt")