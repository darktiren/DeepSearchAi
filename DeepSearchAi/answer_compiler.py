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
import shutil

def compile_answers():
    # Step 1: Get all subfolders within the current folder
    current_dir = os.getcwd()
    subfolders = [f.path for f in os.scandir(current_dir) if f.is_dir()]

    # Step 2 & 3: Access each folder, copy contents of listed_answers.txt, and compile them into all_answers.txt
    all_answers = []
    for folder in subfolders:
        answers_file_path = os.path.join(folder, 'listed_answers.txt')
        if os.path.exists(answers_file_path):
            with open(answers_file_path, 'r') as f:
                all_answers.extend(f.readlines())

    # Step 4: Write compiled answers to all_answers.txt
    with open('all_answers.txt', 'w') as f:
        f.writelines(all_answers)

    # Execute final_answer.py
    os.system('python final_answer.py')

if __name__ == "__main__":
    compile_answers()
