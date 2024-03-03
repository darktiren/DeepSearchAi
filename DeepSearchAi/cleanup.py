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

# Step 1: Delete all subfolders within the folder except 'build'
def delete_subfolders(folder_path):
    for root, dirs, files in os.walk(folder_path, topdown=False):
        for name in dirs:
            if name != 'build':  # Check if the folder name is not 'build'
                subfolder_path = os.path.join(root, name)
                for file in os.listdir(subfolder_path):
                    file_path = os.path.join(subfolder_path, file)
                    if os.path.isfile(file_path):
                        os.remove(file_path)
                os.rmdir(subfolder_path)

# Step 2: Delete answer.txt and all_answers.txt
def delete_files(*files):
    for file in files:
        if os.path.exists(file):
            os.remove(file)

# Step 3: Access web_agent_6.py and ensure line 46 is as specified
def modify_web_agent_6():
    file_path = "web_agent_6.py"
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            script_content = file.read()
        if "www.example.com" not in script_content:
            modified_content = script_content.replace("web_address", "www.example.com")
            with open(file_path, 'w') as file:
                file.write(modified_content)

# Step 4: Call functions to perform cleanup tasks
def main():
    # Step 1
    delete_subfolders(os.getcwd())  # assuming cleanup is being run in the same directory
    # Step 2
    delete_files("answer.txt", "all_answers.txt")
    # Step 3
    modify_web_agent_6()

if __name__ == "__main__":
    main()
