from youtubesearchpython import VideosSearch

path_to_script = "C:/Users/bsimb/Documents/Programmieren_Privat/Python/copilot test/"


def link_from_searchtherm(search):
    """
    Returns the link of the first result of a YouTube search.
    """
    videosSearch = VideosSearch(search, limit=1)

    title = videosSearch.result()['result'][0]['title']



    link = videosSearch.result()['result'][0]['link']
    return [link, title]

def get_mp3_from_youtube(link):
    import yt_dlp as youtube_dl
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
    import shutil
    shutil.move(dest_now, dest_new)

while True:
    search = input("Searchtherm for Video: ")
    return_from_lfs = link_from_searchtherm(search)
    link = return_from_lfs[0]
    title = return_from_lfs[1]
    question = "Video Title: " + title + ", continue or retry? ", link, " (y/n/r)"
    file = title + ".mp3"
    inp = input(question)




    if inp == "y":
        get_mp3_from_youtube(link)
        print("Downloaded")
        #move_file(path_to_script + file, "Z:/1-Musik/03_From_Script")
        break
    elif inp == "r":
        pass
    else:
        print("Exited")
        break
