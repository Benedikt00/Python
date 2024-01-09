import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

import move
import settings
import convert_to_mp3_and_metatadate

import os
from youtubesearchpython import VideosSearch
from pytube import YouTube

# Replace with your own Spotify API credentials
client_id = settings.client_id
client_secret = settings.client_secret

dump_folder = settings.wix_alles_eine
artist_name_file_path = settings.artist_file  # Replace with the path to your text file
root_folder = settings.root_folder

# Initialize the Spotify API client
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


def download_song(song_name, artist_name):
	# Create a folder for the artist if it doesn't exist

	if not os.path.exists(dump_folder):
		os.makedirs(dump_folder)

	# Perform a YouTube search with the song name and artist
	search_query = f"{song_name} {artist_name} audio"
	videos_search = VideosSearch(search_query, limit=1)
	results = videos_search.result()
	if results != 0:
		video_url = results['result'][0]['link']
		# Download the YouTube video as an MP3
		try:
			yt = YouTube(video_url)
			audio_stream = yt.streams.filter(only_audio=True).first()
			mp3_filename = f"{artist_name} - {song_name}.mp3"
			artist_folder = os.path.join(root_folder, artist_name)
			if not os.path.exists(artist_folder):
				os.makedirs(artist_folder)
			audio_stream.download(output_path=artist_folder, filename=mp3_filename)
			convert_to_mp3_and_metatadate.process_mp3_file(os.path.join(artist_folder, mp3_filename))

		except Exception as e:
			return f"Error downloading {song_name}: {str(e)}"

	else:
		return f"No results found for {song_name}"


def download_mp3(artist, songs):
	print(artist)
	# print(songs)
	for i, track in enumerate(songs):
		song = track['name']
		download_song(song, artist)
		print(song)


def get_top_songs(artist_name):
	# Search for the artis
	force = False

	while True:
		results = sp.search(q=artist_name, type='artist')

		if len(results['artists']['items']) == 0:
			print(f"No artist found with the name '{artist_name}'.")
			exit()
		else:
			name_at_sp = results['artists']['items'][0]['name']

			if name_at_sp is not artist_name:
				desicion = input(f"Did you mean: {name_at_sp} y/n/ch: ")
				if desicion == "yy":
					force = True
					break
				if desicion == "y":
					break
				elif desicion == "n":
					return
				elif desicion == 'ch':
					artist_name = input("Enter new name or \"exit\": ")
					if artist_name == "exit":
						return

			else:
				break

	artist = results['artists']['items'][0]
	artist_id = artist['id']

	# Get the top tracks for the artist
	top_tracks = sp.artist_top_tracks(artist_id)

	# print(top_tracks)
	print(f"Top 10 Songs by {artist_name} on Spotify:")
	for i, track in enumerate(top_tracks['tracks'][:20]):
		print(f"{i + 1}. {track['name']}")

	if not force:
		inp = input("Do you want to download these songs y/n/r: ")
		if inp == "y":
			download_mp3(artist_name, top_tracks['tracks'][:20])
		elif inp == "n":
			return
		elif inp == "r":
			get_top_songs(artist)

	else:
		download_mp3(artist_name, top_tracks['tracks'][:20])


def read_file_to_array(file_path):
	try:
		with open(file_path, 'r+') as file:
			lines = file.readlines()
			# Remove newline characters from the end of each line
			lines = [line.strip() for line in lines]
			return lines  # Return as a list (array)
	except FileNotFoundError:
		print(f"The file '{file_path}' was not found.")
		return []
	except Exception as e:
		print(f"An error occurred: {str(e)}")
		return []


# Example usage:

artists = read_file_to_array(artist_name_file_path)

print(artists)

for act_artist in artists:
	try:
		get_top_songs(act_artist)
	except Exception as e:
		print(e)

move.move_files()

if input("Wanna delete File contens?(y/n) ") == "y":
	with open(artist_name_file_path, 'r+') as file:
		file.truncate(0)
