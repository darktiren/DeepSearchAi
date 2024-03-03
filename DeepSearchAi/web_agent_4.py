# Copyright (C) [2024] [Christopher Garner]

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import json
import subprocess
import os

def update_query_counter(file_path):
    # Load JSON data from the file
    with open(file_path, 'r') as f:
        data = json.load(f)
    
    # Update the Current Query Counter to 1
    data['Current Query Counter'] = 1
    
    # Write the updated data back to the file
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)

def execute_script(script_path):
    # Execute the specified Python script
    subprocess.run(["python", script_path])

if __name__ == "__main__":
    # Get the directory path of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # File paths
    web_agent_json_path = os.path.join(script_dir, "web_agent.json")
    web_agent_5_script_path = os.path.join(script_dir, "web_agent_5.py")

    # Task 1: Update the Current Query Counter to 1
    update_query_counter(web_agent_json_path)

    # Task 2: Execute web_agent_5.py
    execute_script(web_agent_5_script_path)

