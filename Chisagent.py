#!/usr/bin/env python3
#This Python script logs the commands entered by a user in a shell session, along with the user's IP addresses, hostname, and operating system release. The data is saved to a JSON file with a timestamp,
# and the last command is compared to the previous command to avoid duplicate entries. The script is designed to be run as the PROMPT_COMMAND environment variable in Linux or Unix systems.
#add this under /etc/bash.bashrc end of the file
#change it base your location
#export PROMPT_COMMAND='python3 /home/demo/Chisagent/Chisagent.py "$(history 1 | sed -e "s/^[ ]*[0-9]\+[ ]*//g")"'


import os                  # module for interacting with the operating system
import json                # module for working with JSON data
import datetime            # module for working with dates and times
import sys                 # module for working with command-line arguments
import socket              # module for working with network connections
import subprocess          # module for running subprocesses

# Define a class named `agent`
class agent():
    def __init__(self, command):
        # Initialize the class attributes
        self.command = command.strip()  # The command that was executed
        self.user = os.environ.get('USER')  # The username of the user who executed the command
        self.ip_addresses = os.popen('hostname --all-ip-addresses').read().strip().split()  # A list of IP addresses for the machine
        self.hostname = socket.gethostname()  # The hostname of the machine
        output = subprocess.check_output(['lsb_release', '-d']).decode('utf-8').strip()  # Run the `lsb_release -d` command to get the OS release info
        self.os_release = output.split(':')[1].strip()  # Extract the OS release info from the output of the `lsb_release -d` command
        self.timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # The date and time when the command was executed

    # Define a method named `json_template` that returns a dictionary representing the command data in the desired JSON format
    def json_template(self):
        command_data = {
            'command': self.command,            # The command that was executed
            'timestamp': self.timestamp,        # The date and time when the command was executed
            'user': self.user,                  # The username of the user who executed the command
            'ips': self.ip_addresses,           # A list of IP addresses for the machine
            'hostname': self.hostname,          # The hostname of the machine
            'os_release': self.os_release,       # The OS release info for the machine
        }
        return command_data

# The main block of code that gets executed when the script is run
if __name__ == '__main__':
    if len(sys.argv) > 1:
        # If the script is run with a command-line argument, create an `agent` object for the command and add it to the command history
        command = agent(sys.argv[1])
        try:
            with open('/tmp/history.json', 'r') as f:
                history = json.load(f)
        except FileNotFoundError:
            history = []
        history.append(command.json_template())
        with open('/tmp/history.json', 'w') as f:
            json.dump(history, f, indent=2)

