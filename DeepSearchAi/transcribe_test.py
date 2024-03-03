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
from tqdm import tqdm
import google.ai.generativelanguage as glm
import google.generativeai as genai

def main():
    # Step 1: Get list of image files in the current directory
    image_files = [f for f in os.listdir() if f.startswith("scroll_") and f.endswith(".png")]

    # Step 2: Initialize Google generative AI model
    api_key = "YOUR_API_KEY_HERE"  # Replace with your actual API key
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-pro-vision')

    # Step 3: Iterate through each image and send to vision model
    for image_file in tqdm(image_files, desc="Processing images", unit="image"):
        # Construct prompt
        prompt = "Please translate this screenshot of a website into text a text-only LLM could interpret. To do this describe in as much detail as possible any images within the website screenshot, use context clues from surrounding text to identify persons and places. Extract all text from the website within the screenshot. The response should be text representation of the Website screenshot, with images replaced by descriptions of the image and a marker to let the model know that part is a summary of a picture."

        # Read image file as bytes
        with open(image_file, "rb") as f:
            image_data = f.read()

        # Generate content
        result = model.generate_content(
            glm.Content(
                parts=[
                    glm.Part(text=prompt),
                    glm.Part(
                        inline_data=glm.Blob(
                            mime_type='image/png',
                            data=image_data
                        )
                    ),
                ],
            ),
            stream=True
        )

        # Resolve response
        result.resolve()

        # Get response text
        response_texts = [part.text for part in result.parts]
        response_text = "\n".join(response_texts)

        # Step 4: Store response in transcribed.txt
        with open("transcribed.txt", "a", encoding="utf-8") as f:  # Specify encoding as utf-8
            f.write(response_text)
            f.write("\n---\n")  # Separator between responses

if __name__ == "__main__":
    main()