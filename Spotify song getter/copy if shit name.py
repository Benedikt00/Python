import os
import shutil
import convert_to_mp3_and_metatadate


# Function to copy files containing a specific name
def copy_files_with_name(src_folder, dest_folder, name_to_search):
    for root, _, files in os.walk(src_folder):
        for file in files:
            if name_to_search in file:
                src_path = os.path.join(root, file)
                dest_path = os.path.join(dest_folder, file)
                shutil.move(src_path, dest_path)
                print(f'Copied {src_path} to {dest_path}')
                convert_to_mp3_and_metatadate.process_mp3_file(dest_path)


if __name__ == "__main__":
    src_folder = r"C:\Users\bsimb\Documents\Programmieren_Privat\Python\Spotify song getter\destination_folder\Dies und jenes"  # Replace with the source folder path
    dest_folder = r"C:\Users\bsimb\Documents\Programmieren_Privat\Python\Spotify song getter\destination_folder"  # Replace with the destination folder path

    name_to_search = "Alan Walker"  # Replace with the name to search

    dest_folder = os.path.join(dest_folder, name_to_search)

    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    copy_files_with_name(src_folder, dest_folder, name_to_search)
