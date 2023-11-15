from pydub import AudioSegment
from mutagen.id3 import ID3, TIT2, TPE1

from moviepy.editor import *

def MP4ToMP3(mp4, mp3):
    audio = AudioSegment.from_file(mp4, format="mp4")
    audio.export(mp3, format="mp3")

def remove_artist_from_filepath(filepath):
    # Split the file path into directory and filename
    directory, filename = os.path.split(filepath)

    # Split the filename into artist and title
    artist, title = filename.split('-', 1)

    # Remove leading and trailing whitespaces
    artist = artist.strip()
    title = title.strip()

    # Construct the new file path without the artist
    new_filepath = os.path.join(directory, title)

    return new_filepath



# Function to convert and edit metadata of an MP3 file
def process_mp3_file(mp3_file):
    try:
        MP4ToMP3(mp3_file, mp3_file)
        filename = os.path.basename(mp3_file)
        artist, title = filename.split('-', 1)
        artist = artist.strip()
        title = title.strip().split('.mp', 1)
        print(filename)

        audio = AudioSegment.from_mp3(mp3_file)

        # Create a new MP3 file with updated metadata
        audio.export(mp3_file, format="mp3", tags={'artist': artist, 'title': title})


        # Update ID3 tags
        audio = ID3(mp3_file)
        audio.add(TIT2(text=title))
        audio.add(TPE1(text=artist))
        audio.save()

        os.rename(mp3_file, remove_artist_from_filepath(mp3_file))
    except Exception as e:
        print("Vermutlich schon convertiert ", mp3_file)


# Function to process a folder and its subfolders
def process_folder(folder_path):
    for root, dirs, files in os.walk(folder_path):
        print(files)
        for file in files:
            if file.lower().endswith('.mp3'):
                mp3_file = os.path.join(root, file)
                process_mp3_file(mp3_file)


# Main function
def main():
    folder_path = r'C:\Users\bsimb\Music\Musik'  # Replace with the path to the root folder
    process_folder(folder_path)

if __name__ == "__main__":
    main()