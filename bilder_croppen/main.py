from PIL import Image

# Open the image file
image = Image.open(r"C:\Users\bsimb\Documents\Bilder Papa\Dubai\Scannen.jpg")

# Get the dimensions of the image
width, height = image.size

# Set the number of pixels to crop from each side
left_crop = 300
right_crop = 300

# Set the number of pixels to crop from the top and bottom
top_crop = 0
bottom_crop = 900

# Calculate the new dimensions of the image
new_width = width - left_crop - right_crop
new_height = height - top_crop - bottom_crop

# Crop the image
cropped_image = image.crop((left_crop, top_crop, width - right_crop, height - bottom_crop))

# Save the cropped image
cropped_image.save(r"C:\Users\bsimb\Documents\Bilder Papa\Dubai\Scannencroptest.jpg")

