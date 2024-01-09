import os
import eyed3


# Function to change metadata for a single MP3 file
def change_metadata(file_path):
	try:
		audiofile = eyed3.load(file_path)

		audiofile.tag.artist = audiofile.tag.artist.replace(" feat.", ",")
		print(f"Changed metadata for {file_path}")
		audiofile.tag.save()
	except Exception as e:
		print(file_path, " ------------------------ Error")


# Function to process all MP3 files in a folder and its subfolders
def process_files_in_folder(folder_path):
	for root, _, files in os.walk(folder_path):
		for file in files:
			if file.endswith(".mp3"):
				file_path = os.path.join(root, file)
				change_metadata(file_path)



# Specify the folder containing the MP3 files
folder_path = r"C:\Users\bsimb\Music\Musik"

# Check if the folder exists
if os.path.exists(folder_path):
	process_files_in_folder(folder_path)
else:
	print("The specified folder does not exist.")