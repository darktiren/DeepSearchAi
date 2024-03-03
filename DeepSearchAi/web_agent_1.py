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
import os
import google.generativeai as genai

def main():
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Step 1: Access web_agent.json & Copy Search Key
    with open(os.path.join(script_dir, "web_agent.json"), "r") as f:
        data = json.load(f)
    search_query = data["Search"]

    # Step 2: Construct Prompt
    prompt = f"You are a part of an autonomous system designed for targeted web searches. Analyse the following search request to generate a short numbered list (max of 5) of possible search queries to perform in order to complete the request: '{search_query}'."
    data["Prompt"] = prompt

    # Step 3: Store Prompt in web_agent.json
    with open(os.path.join(script_dir, "web_agent.json"), "w") as f:
        json.dump(data, f, indent=4)

    # Step 4: Send Prompt to Google gemini-pro model
    api_key = "YOUR_API_KEY_HERE"  # Replace 'YOUR_API_KEY_HERE' with your actual API key
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-pro')  
    result = model.generate_content(prompt)
    
    # Convert result.parts to a list of strings
    response_texts = [part.text for part in result.parts]

    # Join the list of strings into a single string
    response_text = "\n".join(response_texts)
    
    # Step 5: Store Response in web_agent.json
    data["Response"] = response_text
    with open(os.path.join(script_dir, "web_agent.json"), "w") as f:
        json.dump(data, f, indent=4)

    # Step 6: Execute web_agent_2.py
    os.system("python " + os.path.join(script_dir, "web_agent_2.py"))

if __name__ == "__main__":
    main()

