import os
import convert_to_mp3_and_metatadate

# Specify the folder you want to iterate through
folder_path = r"C:\Users\bsimb\Documents\Programmieren_Privat\Python\Spotify song getter\destination_folder\CRO"

# Check if the folder exists
if os.path.exists(folder_path):
    # Iterate through all files in the folder
    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            # Call your processing function on each file
            convert_to_mp3_and_metatadate.process_mp3_file(file_path)
else:
    print("The specified folder does not exist.")