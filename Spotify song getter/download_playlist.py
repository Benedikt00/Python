import csv
import os
import re
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

import pandas as pd
from youtubesearchpython import VideosSearch
from pytube import YouTube

from move import move_files

import settings


OUTPUT_FILE_NAME = settings.output_csv
download_folder = settings.wix_alles_eine  # Replace with your desired download folder

# change for your target playlist
PLAYLIST_LINK = "https://open.spotify.com/playlist/7ndsEsh5BfeJsR7nv4OCUT?si=6a42758843e74644"

# authenticate
client_credentials_manager = SpotifyClientCredentials(
	client_id="19683b6bf6654fa1bcadd6dd0fa80c1d", client_secret="9f401ab9eed74abd9e327869e1e59a64"
)

# create spotify session object
session = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# get uri from https link
if match := re.match(r"https://open.spotify.com/playlist/(.*)\?", PLAYLIST_LINK):
	playlist_uri = match.groups()[0]
else:
	raise ValueError("Expected format: https://open.spotify.com/playlist/...")

# get list of tracks in a given playlist (note: max playlist length 100)
tracks = session.playlist_items(playlist_uri)["items"]

# create csv file
with open(OUTPUT_FILE_NAME, "w", encoding="utf-8") as file:
	writer = csv.writer(file)

	# write header column names
	writer.writerow(["track", "artist"])

	# extract name and artist
	for track in tracks:
		name = track["track"]["name"]
		artists = ", ".join(
			[artist["name"] for artist in track["track"]["artists"]]
		)

		writer.writerow([name, artists])



# Define the input CSV file and folder for downloaded MP3s


# Create the download folder if it doesn't exist
if not os.path.exists(download_folder):
	os.makedirs(download_folder)

# Read the CSV file into a DataFrame
df = pd.read_csv(OUTPUT_FILE_NAME)

# Iterate through each row in the DataFrame
for index, row in df.iterrows():
	artist = row['artist']
	song_title = row['track']
	# Perform a YouTube search with the artist, song title, and "lyrics" keyword
	search_query = f"{artist} {song_title} lyrics"
	videos_search = VideosSearch(search_query, limit=1)
	results = videos_search.result()
	if results:
		try:
			video_url = results['result'][0]['link']
			print(results['result'][0]['title'])
			# Download the YouTube video as an MP3

			yt = YouTube(video_url)
			audio_stream = yt.streams.filter(only_audio=True).first()
			mp3_filename = f"{artist} - {song_title}.mp3"
			mp3_filepath = os.path.join(download_folder, mp3_filename)
			audio_stream.download(output_path=download_folder, filename=mp3_filename)
			print(f"    Downloaded: {mp3_filename}")
		except Exception as e:
			print(f"Error downloading {artist} - {song_title}: {str(e)}")
	else:
		print(f"No results found for {artist} - {song_title}")
print("Download completed.")

move_files()

print("Moved Files")

# Optionally, you can move the downloaded MP3s to another folder here
