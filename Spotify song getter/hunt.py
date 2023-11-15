import os

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

# Example usage:
filepath = r"C:\Users\bsimb\Documents\Programmieren_Privat\Python\Spotify song getter\destination_folder\David Guetta\David Guetta - Love Tonight (David Guetta Remix Edit).mp3"
new_filepath = remove_artist_from_filepath(filepath)
print("Original File Path:", filepath)
print("Modified File Path:", new_filepath)