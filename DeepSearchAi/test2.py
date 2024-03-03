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

from PIL import Image
import os

# Get list of screenshot files in the current directory
screenshot_files = sorted([file for file in os.listdir() if file.endswith(".png")])

# Load the first image to get dimensions
first_image = Image.open(screenshot_files[0])
image_width, image_height = first_image.size

# Create a blank combined image
combined_image = Image.new("RGB", (image_width, image_height * len(screenshot_files)))

# Paste each screenshot into the combined image
for i, file in enumerate(screenshot_files):
    image = Image.open(file)
    combined_image.paste(image, (0, i * image_height))

# Save the combined image
combined_image.save("combined_image.png")

# Convert the combined image to PDF
combined_image.save("combined_pdf.pdf", "PDF", resolution=100.0, save_all=True)
