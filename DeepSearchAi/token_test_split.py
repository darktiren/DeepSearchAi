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
import requests

# Function to count tokens using Google API
def count_tokens(text):
    api_key = "YOUR_API_KEY_HERE"  # Replace with your API key
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:countTokens?key=" + api_key
    data = {
        "contents": [{"parts": [{"text": text}]}]
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, headers=headers, json=data)
    result = response.json()
    return result['totalTokens']

# Function to split text into multiple files
def split_text(input_text, max_tokens_per_file):
    num_files = len(input_text) // max_tokens_per_file + 1
    for i in range(num_files):
        start = i * max_tokens_per_file
        end = min((i + 1) * max_tokens_per_file, len(input_text))
        output_text = input_text[start:end]
        with open(f"transcribed_{i+1}.txt", "w", encoding="utf-8") as file:
            file.write(output_text)

# Read content from transcribed.txt
with open("transcribed.txt", "r", encoding="utf-8") as file:
    content = file.read()

# Count tokens
total_tokens = count_tokens(content)

# Split into multiple files if over 15,000 tokens
if total_tokens > 15000:
    split_text(content, 10000)
else:
    with open("transcribed_1.txt", "w", encoding="utf-8") as file:
        file.write(content)