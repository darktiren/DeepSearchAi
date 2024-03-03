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

import time
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import cv2
from skimage.metrics import structural_similarity as ssim

# Function to scroll down one page segment
def scroll_down(driver, window_height):
    driver.execute_script(f"window.scrollBy(0, {window_height});")
    time.sleep(2)  # Wait for the page to load

# Function to scroll up 20% of the current page segment
def scroll_up_partial(driver, window_height):
    scroll_distance = int(window_height * 0.2)
    if scroll_distance < 1:  # Ensure minimum scroll distance
        scroll_distance = 1
    driver.execute_script(f"window.scrollBy(0, -{scroll_distance});")
    time.sleep(1)  # Wait for the page to load

# Function to scroll to the top of the page
def scroll_to_top(driver):
    driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(3)  # Wait for the page to load

# Function to compare images
def compare_images(img1, img2):
    # Load images
    image1 = cv2.imread(img1)
    image2 = cv2.imread(img2)

    # Convert images to grayscale
    gray_image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    gray_image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    # Compute Structural Similarity Index (SSI)
    ssi = ssim(gray_image1, gray_image2)

    return ssi >= 0.8  # Return True if SSI is 0.6 or greater, indicating a match of 60% or more


# Launch the browser (Firefox in this case)
driver = webdriver.Firefox()

# Open the website (with retry)
retry_count = 3
for i in range(retry_count):
    try:
        driver.get("www.example.com")  # Replace with your website
        break  # If successful, break the loop
    except WebDriverException as e:
        print("Error occurred:", e)
        if i < retry_count - 1:
            print("Retrying...")
            time.sleep(5)  # Wait before retrying
        else:
            print("Max retry attempts reached. Exiting...")
            driver.quit()
            exit()

time.sleep(4)  # Wait for the page to load

# Get the window height
window_height = driver.execute_script("return window.innerHeight")

# Take initial screenshot upon loading the site
driver.save_screenshot(f"scroll_1.png")
prev_screenshot = f"scroll_1.png"

# Initialize scroll counter
scroll_counter = 2

# Start loop to repeatedly scroll down until the bottom
while True:
    try:
        # Attempt to scroll down one page segment
        scroll_down(driver, window_height)
        
        # Scroll back up 20% of the current page segment
        scroll_up_partial(driver, window_height)
        
        # Save screenshot after scroll up
        current_screenshot = f"scroll_{scroll_counter}.png"
        driver.save_screenshot(current_screenshot)
        
        # Compare current screenshot with the previous one
        similarity = compare_images(prev_screenshot, current_screenshot)
        if similarity == 1.0:  # If images are identical
            break
        
        prev_screenshot = current_screenshot
        
        # Increment scroll counter
        scroll_counter += 1
    except WebDriverException as e:
        print("Error occurred:", e)
        break  # Break the loop if an error occurs
    
    # Check if the page is at the bottom
    scroll_position = driver.execute_script("return window.scrollY")
    scroll_height = driver.execute_script("return document.body.scrollHeight")
    if scroll_position + window_height >= scroll_height:
        break  # If at the bottom, break the loop

# Scroll back to the top of the page
scroll_to_top(driver)

# Close the browser
driver.quit()