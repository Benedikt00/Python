import spotipy
import os
from spotipy.oauth2 import SpotifyClientCredentials
from pytube import YouTube
from youtubesearchpython import VideosSearch

import settings
import convert_to_mp3_and_metatadate as ctmp3

client_id = settings.client_id
client_secret = settings.client_secret

dump_folder = settings.wix_alles_eine

# Initialize the Spotify API client
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


def search_spotify_song(song_name, artist_name):
    query = f"{song_name} artist:{artist_name}"
    results = sp.search(q=query, type='track', limit=1)

    if results['tracks']['items']:
        track = results['tracks']['items'][0]
        return track

    return None

# Function to download a song from YouTube
def download_song_youtube(song_name, artist_name):
    # Perform a YouTube search for the song name and artist
    search_query = f"{song_name} {artist_name} audio"
    video_url = VideosSearch(search_query, limit=1).result()['result'][0]['link']
    yt = YouTube(video_url)
    audio_stream = yt.streams.filter(only_audio=True).first()
    mp3_filename = f"{artist_name} - {song_name}.mp3"
    print("Filename: ", mp3_filename)
    if input("Wanna change (y/n)? ") == "y":
        mp3_filename = input("New Filename: ")
    mp3_filepath = os.path.join(dump_folder, mp3_filename)
    audio_stream.download(output_path=dump_folder, filename=mp3_filename)
    ctmp3.process_file(mp3_filepath)
    return mp3_filepath


# Main function
def main():
    song_name = input("Enter song name: ")
    artist_name = input("Enter artist name: ")

    choice = input("Search on Spotify (S) or YouTube (Y)? ").upper()

    if choice == 'S':
        # Search for the song on Spotify
        track = search_spotify_song(song_name, artist_name)

        if track:
            print(f"Song found on Spotify: {track['name']} by {', '.join(artist['name'] for artist in track['artists'])}")
            mp3_filepath = download_song_youtube(track['name'], track['artists'][0]['name'])

            if mp3_filepath:
                print(f"Downloaded MP3: {mp3_filepath}")
            else:
                print("Failed to download MP3 from YouTube.")
        else:
            print("Song not found on Spotify.")
    elif choice == 'Y':
        mp3_filepath = download_song_youtube(song_name, artist_name)
        if mp3_filepath:
            print(f"Downloaded MP3 from YouTube: {mp3_filepath}")
        else:
            print("Failed to download MP3 from YouTube.")
    else:
        print("Invalid choice. Please enter 'S' for Spotify or 'Y' for YouTube.")

    import move

    move.move_files()


if __name__ == "__main__":
    main()