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

import subprocess
import os

# Step 1: Copy the contents of the answer.txt file
with open('answer.txt', 'r') as file:
    copied_contents = file.read().strip()

# Step 2: Display copied contents within the cmd prompts
print(f"Search Query/Question Results: '{copied_contents}'")

# Step 3: Ask user if they want to save the response
response = input("Do you want to save this response? (Y/N): ").strip().upper()

if response == 'Y':
    save_location = input("Type a save location outside the DeepSearchAi folder: ")
    filename = input("Enter the filename (without extension): ").strip()
    full_path = os.path.join(save_location, filename + '.txt')
    with open(full_path, 'w') as save_file:
        save_file.write(copied_contents)

# Step 4: Ask if the user would like to conduct a new search
new_search = input("Would you like to conduct a new search? (Y/N): ").strip().upper()

if new_search == 'N':
    subprocess.run(["python", "cleanup.py"])
else:
    subprocess.Popen(["cmd", "/c", "start", "deepsearchai.exe"])
    subprocess.run(["python", "cleanup.py"])
