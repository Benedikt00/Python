import os
import eyed3


def set_artist_to_prefix(filename):
    # Parse the file name to get the artist prefix
    basename = os.path.basename(filename)
    artist_prefix, _ = os.path.splitext(basename)[0].split("-", 1)
    artist_prefix = artist_prefix.strip()  # Remove leading and trailing whitespace

    # Load the MP3 file and set the artist metadata if it exists
    audiofile = eyed3.load(filename)
    print(audiofile)
    audiofile.tag.artist = artist_prefix
    audiofile.tag.save()

def process_directory(root_directory):
    # Recursively process all MP3 files in subdirectories of the root directory
    for root, _, files in os.walk(root_directory):
        for filename in files:
            if filename.endswith(".mp3"):
                mp3_file = os.path.join(root, filename)
                set_artist_to_prefix(mp3_file)


if __name__ == "__main__":
    target_directory = 'destination_folder'  # Replace with the path to your directory
    process_directory(target_directory)