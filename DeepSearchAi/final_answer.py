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
import google.generativeai as genai
import subprocess

def main():
    try:
        # Step 1: Access all_answers.txt
        if not os.path.exists("all_answers.txt"):
            raise FileNotFoundError("all_answers.txt not found in the current directory")
        with open("all_answers.txt", "r") as f:
            all_answers = f.read().strip()

        # Step 2: Access web_agent.json & Copy Search Key
        if not os.path.exists("web_agent.json"):
            raise FileNotFoundError("web_agent.json not found in the current directory")
        with open("web_agent.json", "r") as f:
            data = json.load(f)
        search_query = data.get("Search", "") 

        # Step 3: Craft the prompt
        prompt = f"""Please attempt to answer the search query/question as in depth as possible using the provided accumulated information from multiple sources. Be as descriptive as possible. SEARCH QUERY/QUESTION: '{search_query}'. GATHERED DATA: '{all_answers}'. REMINDER TO THE MODEL: Please attempt to answer the search query/question as in depth as possible using the provided accUmlated information from multiple sources. Be as descriptive as possible."""

        # Step 4: Send the prompt to the model 
        api_key = "YOUR_API_KEY_HERE"  # Replace 'YOUR_API_KEY_HERE' with your actual API key
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-pro')  

        # Safety settings to block none for every category
        safety_settings = {'HARM_CATEGORY_SEXUALLY_EXPLICIT': 'block_none',
                           'HARM_CATEGORY_HATE_SPEECH': 'block_none',
                           'HARM_CATEGORY_HARASSMENT': 'block_none',
                           'HARM_CATEGORY_DANGEROUS_CONTENT': 'block_none'}

        retry_count = 0
        while retry_count < 3:
            try:
                result = model.generate_content(prompt)
                break  # Exit the loop on success
            except Exception as e:  
                if "google.generativeai.types.generation_types.BlockedPromptException" in str(e) and "block_reason: OTHER" in str(e):
                    retry_count += 1
                    print(f"Error occurred: {e}. Retrying... (Attempt {retry_count}/3)")
                else:
                    print(f"Error occurred: {e}. Skipping generation.")
                    break 
            else:
                print("Maximum retries reached. Skipping generation.")
                continue  # Skip to next iteration without writing response

        # Step 5: Store the response (if successful generation)
        if result: 
            response_texts = [part.text for part in result.parts]
            response_text = "\n".join(response_texts)
            with open("answer.txt", "w") as f:
                f.write(response_text)

            # Execute display.py
            subprocess.run(["python", "display.py"])

    except (FileNotFoundError, json.JSONDecodeError, Exception) as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
