from pydub import AudioSegment
from mutagen.id3 import ID3, TIT2, TPE1

from moviepy.editor import *


def MP4ToMP3(mp4, mp3):
    audio = AudioSegment.from_file(mp4, format="mp4")
    audio.export(mp3, format="mp3")


def remove_artist_from_filepath(filepath):
    directory, filename = os.path.split(filepath)
    artist, title = filename.split(' - ', 1)
    title = title.strip()
    new_filepath = os.path.join(directory, title)

    return new_filepath


def process_mp3_file(mp3_file):
    try:
        MP4ToMP3(mp3_file, mp3_file)
        filename = os.path.basename(mp3_file)
        artist, title = filename.split(' - ', 1)
        artist = artist.strip().replace(",", ";")
        artist = artist.strip().replace(",", "&")
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
        print(" --------------------------- Vermutlich schon convertiert oder kaputt ", mp3_file, " ---------------------------")


def process_file(file_path):
    if file_path.lower().endswith('.mp3'):
        process_mp3_file(file_path)
        #os.remove(file_path)


# Main function
def main():
    file_path = r'C:\Users\bsimb\Music\Musik\Dies und jenes'  # Replace with the path to the root folder
    process_file(file_path)


if __name__ == "__main__":
    main()