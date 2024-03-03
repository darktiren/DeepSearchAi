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
import subprocess
import tkinter as tk
from tkinter import messagebox

def check_api_json():
    if not os.path.exists('api.json'):
        messagebox.showinfo("DeepSearchAi Installation Required", "Please install DeepSearchAi by executing the install script within this folder.")
        return False
    return True

def get_search_query():
    while True:
        query = input("Enter your search query/question here. Deepsearch will analyze 25 websites to compile an answer, process may take 20-40 minutes: ")
        if query.strip():
            return query
        else:
            print("Please enter something!")

def update_web_agent_json(query):
    with open('web_agent.json', 'r') as file:
        data = json.load(file)
    
    data['Search'] = query

    with open('web_agent.json', 'w') as file:
        json.dump(data, file, indent=4)

def execute_web_agent_1():
    subprocess.run(['python', 'web_agent_1.py'])

def main():
    if not check_api_json():
        return
    
    query = get_search_query()
    update_web_agent_json(query)
    execute_web_agent_1()

if __name__ == "__main__":
    main()
