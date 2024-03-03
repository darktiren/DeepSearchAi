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
import json
import tkinter as tk  # For simple GUI
from tkinter import messagebox
import subprocess

# **1. API File Management**
def manage_api_file():
    api_file = "api.json"
    if not os.path.exists(api_file):
        with open(api_file, 'w') as f:
            json.dump({"API": ""}, f)

# **2.  Popup UI for API Key**
def get_api_key():
    def submit_key():
        api_key = api_entry.get()
        with open("api.json", 'r+') as f:
            data = json.load(f)
            data["API"] = api_key
            f.seek(0)
            json.dump(data, f, indent=4)
        window.destroy()

    window = tk.Tk()
    window.title("Google AI API Setup")

    tk.Label(window, text="Please enter your Google AI API key:").pack()
    api_entry = tk.Entry(window)
    api_entry.pack()

    setup_link = "https://console.cloud.google.com/apis/dashboard"  # Replace with the actual link
    tk.Label(window, text=f"Need to set up an API key? Visit {setup_link}").pack()

    tk.Button(window, text="Submit", command=submit_key).pack()
    window.mainloop()

# **3. Update Scripts with API Key**
def update_scripts():
    api_file = "api.json"
    with open(api_file, 'r') as f:
        data = json.load(f)
    api_key = data["API"]

    for filename in os.listdir():
        if filename.endswith(".py") and filename != 'install.py':
            with open(filename, 'r+') as f:
                contents = f.read()
                contents = contents.replace("YOUR_API_KEY_HERE", api_key)
                f.seek(0)
                f.write(contents)
                f.truncate()

# **4. Requirements Handling**
def handle_requirements():
    if not os.path.exists("requirements.txt"):
        messagebox.showerror("Error", "requirements.txt not found. Please redownload from GitHub.")
        return

    try:
        subprocess.check_call(["pip", "install", "-r", "requirements.txt"])
        print("DeepSearchAi install successful")  # Output to cmd
    except subprocess.CalledProcessError:
        print("DeepSearchAi install unsuccessful")  # Output to cmd

# **5. Create Executable**
def create_executable():
    try:
        os.system('pyinstaller --onefile --icon=icon.png --console main.py')
        print("Executable creation successful")
        # Move the executable to the parent directory
        shutil.move(os.path.join('dist', 'main.exe'), 'DeepSearchAI.exe')
        # Remove the now empty 'dist' directory
        os.rmdir('dist')
        print("Executable moved successfully")
    except Exception as e:
        print("Executable creation or moving unsuccessful:", e)

# Main Execution
manage_api_file()
get_api_key()
update_scripts()
handle_requirements()
create_executable()