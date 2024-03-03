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
import google.generativeai as genai  # Import generative AI module

def main():
    # Step 1: Create a list of all subfolders
    subfolders = [f.path for f in os.scandir('.') if f.is_dir()]

    # Step 2: Access web_agent.json and copy the contents of the Search key
    with open("web_agent.json", "r") as f:
        data = json.load(f)
    search_query = data["Search"]

    for folder in subfolders:
        os.chdir(folder)  # Step 3a: Access the folder

        # Step 3b: Create a list of all transcribed_'number'.txt files within the folder
        transcribed_files = [f for f in os.listdir('.') if f.startswith("transcribed_") and f.endswith(".txt")]

        for file in transcribed_files:
            with open(file, "r", encoding="utf-8") as f:  # Specify encoding as utf-8
                file_content = f.read()

            # Step 3c: Craft and send the prompt to the model
            prompt = f"Using the following website contents please try to answer in detail the following search query/question: QUERY/QUESTION: '{search_query}' WEBSITE CONTENTS: '{file_content}' REMINDER TO MODEL: Attempt to answer in detail the search query/question using the supplied contents from a website: '{search_query}' IMPORTANT NOTE FOR MODEL: THE CONTENTS MOST LIKELY WILL NOT DIRECTLY ANSWER THE QUERY, YOU MUST ATTEMPT TO ANSWER BASED ON THE CONTENTS PROVIDED BY INFERENCE AND LOGIC INTERPRETATIONS."

            # Step 4: Configure API key and communicate with the model
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
                    result = model.generate_content(prompt, safety_settings=safety_settings)
                    break
                except Exception as e:
                    if "google.generativeai.types.generation_types.BlockedPromptException" in str(e) and "block_reason: OTHER" in str(e):
                        retry_count += 1
                        print(f"Error occurred: {e}. Retrying... (Attempt {retry_count}/3)")
                    else:
                        print(f"Error occurred: {e}. Skipping to next image.")
                        break
            else:
                print("Maximum retries reached. Skipping to next image.")
                continue

            # Convert result.parts to a list of strings
            response_texts = [part.text for part in result.parts]

            # Join the list of strings into a single string
            response_text = "\n".join(response_texts)
            
            # Step 5: Store Response in listed_answers.txt
            with open("listed_answers.txt", "a") as f:
                f.write("\n\n--- New Response ---\n\n")
                f.write(f"Transcribed file: {file}\n")
                f.write(response_text + "\n\n")

        os.chdir('..')  # Step 3: Move back to the parent directory

    # Execute answer_compiler.py after returning to the original folder
    os.system("python answer_compiler.py")

if __name__ == "__main__":
    main()
