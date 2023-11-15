import os
from PIL import Image

def crop_jpgs_in_folder(folder_path):
    # List all the files in the folder
    file_list = os.listdir(folder_path)

    # Filter out only the jpg files
    jpg_list = [file for file in file_list if file.endswith('.jpg')]

    # Loop through each jpg file and crop it
    for jpg_file in jpg_list:
        # Open the image file
        image_path = os.path.join(folder_path, jpg_file)
        image = Image.open(image_path)

        # Get the dimensions of the image
        width, height = image.size

        # Set the number of pixels to crop from each side
        left_crop = 320
        right_crop = 320

        # Set the number of pixels to crop from the top and bottom
        top_crop = 0
        bottom_crop = 850

        # Calculate the new dimensions of the image
        new_width = width - left_crop - right_crop
        new_height = height - top_crop - bottom_crop

        # Crop the image
        cropped_image = image.crop((left_crop, top_crop, width - right_crop, height - bottom_crop))

        # Save the cropped image
        cropped_image.save(os.path.join(folder_path, 'C' + jpg_file))

crop_jpgs_in_folder(r"C:\Users\bsimb\Documents\Bilder Papa\Dubai2")