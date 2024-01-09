import os
import shutil
from convert_to_mp3_and_metatadate import process_file
from collections import defaultdict
import settings


# Specify the source folder containing the files
def has_duplicate_prefix(folder_path, prefix_to_check):
    # Create a dictionary to store counts of prefixes
    prefix_counts = {}

    # Iterate through all files in the folder
    for filename in os.listdir(folder_path):
        if ' - ' in filename:
            prefix, _ = filename.split(' - ', 1)
            prefix = prefix.strip()  # Remove leading and trailing whitespace

            # Count the occurrence of each prefix
            if prefix not in prefix_counts:
                prefix_counts[prefix] = 1
            else:
                prefix_counts[prefix] += 1

    # Check if the specified prefix appears more than once
    if prefix_to_check in prefix_counts and prefix_counts[prefix_to_check] > 1:
        return True  # There are duplicate prefixes for the specified prefix

    return False


def move_files():
    wix_alles_eine = settings.wix_alles_eine  # Replace with the path to your source folder
    destination_root = settings.root_folder  # Replace with the path to your destination folder

    only_sort = False

    # Create a list of all files in the source folder
    files = os.listdir(wix_alles_eine)

    # Create a dictionary to store file paths for each artist
    artist_files = {}

    # Iterate through the files and group them by artist
    for file in files:
        if ' - ' in file:
            try:
                artist, _ = file.split(' - ', 1)
                print(artist)
            except ValueError:
                print(file)
                print(file.split(' - ', 1))
            artist = artist.strip()  # Remove leading and trailing whitespace

            # Create a list of files for each artist
            if artist not in artist_files:
                artist_files[artist] = []
            artist_files[artist].append(file)

    if not only_sort:

        # Create artist folders and copy files
        for artist, files in artist_files.items():
            if has_duplicate_prefix(wix_alles_eine, artist) or os.path.exists(os.path.join(destination_root, artist)):
                artist_folder = os.path.join(destination_root, artist)

                # Create the artist folder if it doesn't exist
                if not os.path.exists(artist_folder):
                    os.makedirs(artist_folder)

                # Copy files to the artist folder
                for file in files:
                    source_path = os.path.join(wix_alles_eine, file)
                    destination_path = os.path.join(artist_folder, file)
                    shutil.copy(source_path, destination_path)

                    process_file(destination_path)


    # Specify the destination folder for single files

    if not os.path.exists(wix_alles_eine):
        os.makedirs(wix_alles_eine)

    # Iterate through all subfolders in the source folder
    for root, dirs, files in os.walk(destination_root):
        for dir_name in dirs:
            folder_path = os.path.join(root, dir_name)
            folder_contents = os.listdir(folder_path)

            # Check if the folder contains only one element (file or subfolder)
            if len(folder_contents) == 1:
                item_name = folder_contents[0]
                item_path = os.path.join(folder_path, item_name)

                # Check if the item is a file (not a subfolder)
                if os.path.isfile(item_path):
                    # Move the file to the destination folder
                    destination_path = os.path.join(wix_alles_eine, item_name)
                    shutil.move(item_path, destination_path)

                    # Remove the old folder after moving the file
                    #os.rmdir(folder_path)



    # Create a dictionary to store files based on their prefix
    files_by_prefix = defaultdict(list)

    # Iterate through all files in the source folder
    for filename in os.listdir(wix_alles_eine):
        if ' - ' in filename:
            prefix, _ = filename.split(' - ', 1)
            prefix = prefix.strip()  # Remove leading and trailing whitespace

            # Add the file to the list for the corresponding prefix
            files_by_prefix[prefix].append(filename)

    # Iterate through the prefixes and move files if there are more than one
    for prefix, filenames in files_by_prefix.items():
        if len(filenames) > 1:
            # Check if an outside folder with the same prefix exists

            #delete old files
            for filename in filenames:
                source_path = os.path.join(wix_alles_eine, filename)
                os.remove(source_path)


if __name__ == '__main__':
    move_files()