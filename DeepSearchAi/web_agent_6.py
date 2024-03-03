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

import os
import json
import shutil
import re
import subprocess

# Define files to copy
files_to_copy = ["test.py", "test2.py", "transcribe_test.py", "token_test_split.py"]

# Step 1: Access web_agent.json and get the current query counter value
script_directory = os.path.dirname(os.path.realpath(__file__))
json_path = os.path.join(script_directory, "web_agent.json")

with open(json_path) as json_file:
    data = json.load(json_file)
    current_query_counter = data["Current Query Counter"]

# Formulate the filename for query'value'.json
query_json_filename = f"query{current_query_counter}.json"
query_json_path = os.path.join(script_directory, query_json_filename)

# Step 2: Get the current website counter value
with open(query_json_path) as query_json_file:
    query_data = json.load(query_json_file)
    current_website_counter = query_data["Current Website Counter"]

# Step 3: Create a folder based on the web address
website_value_key = f"Website {current_website_counter}"
web_address = query_data.get(website_value_key, "")  # Get the website address or default to empty string if not found
folder_name = re.sub(r'\W+', '_', web_address)  # Replace special characters with '_'
folder_path = os.path.join(script_directory, folder_name)

# Create the folder if it doesn't exist
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# Step 4: Copy necessary files into the newly created folder
for file in files_to_copy:
    shutil.copy(os.path.join(script_directory, file), folder_path)

# Step 5: Modify test.py script with the web address
test_script_path = os.path.join(folder_path, "test.py")
if os.path.exists(test_script_path):
    with open(test_script_path, 'r') as f:
        script_content = f.read()
    modified_content = script_content.replace("www.example.com", web_address)
    with open(test_script_path, 'w') as f:
        f.write(modified_content)

# Step 6: Execute each copied file one by one from within the folder
for file in files_to_copy:
    file_path = os.path.join(folder_path, file)
    os.chdir(folder_path)  # Change working directory to the created folder
    subprocess.run(["python", file_path])

# Step 7: Increase the value of the Current Website Counter key by 1
query_data["Current Website Counter"] += 1

with open(query_json_path, 'w') as query_json_file:
    json.dump(query_data, query_json_file, indent=4)

# Step 8: Execute web_agent_5.py
os.chdir(script_directory)  # Change working directory back to the original directory
web_agent_5_path = os.path.join(script_directory, "web_agent_5.py")
subprocess.run(["python", web_agent_5_path])
