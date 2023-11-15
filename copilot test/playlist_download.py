from pytube import Playlist
import yt_dlp as youtube_dl
from youtubesearchpython import VideosSearch
import shutil
import os

def get_playlist_urls(URL_PLAYLIST):
	# Retrieve URLs of videos from playlist
	playlist = Playlist(URL_PLAYLIST)
	print('Number Of Videos In playlist: %s' % len(playlist.video_urls))

	urls = []
	for url in playlist:
		urls.append(url)

	return urls



path_to_script = "C:/Users/bsimb/Documents/Programmieren_Privat/Python/copilot test/"

save_path = "C:/Users/bsimb/Music/Youtube_steal"

def link_from_searchtherm(search):
	"""
	Returns the link of the first result of a YouTube search.
	"""
	videosSearch = VideosSearch(search, limit=1)
	title = videosSearch.result()['result'][0]['title']
	link = videosSearch.result()['result'][0]['link']
	return [link, title]

def get_mp3_from_youtube(link):

	ydl_opts = {
		'format': 'bestaudio/best',
		'outtmpl': '%(title)s.%(ext)s',
		'postprocessors': [{
			'key': 'FFmpegExtractAudio',
			'preferredcodec': 'mp3',
			'preferredquality': '192',
		}],
	}
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
		ydl.download([link])

def move_file(dest_now, dest_new):

	shutil.move(dest_now, dest_new)



playlist = "https://www.youtube.com/playlist?list=PLhf1mWIWCddvnjq542bzzDu-crxabYLYQ"

urls = get_playlist_urls(playlist)
for i in urls:
	get_mp3_from_youtube(i)

# giving file extension
ext = ('.mp3')

# iterating over all files
for files in os.listdir(path_to_script):
	if files.endswith(ext):
		print(files)
		filename = save_path+"/"+files

		move_file(path_to_script + "/" + files, filename)
	else:
		continue