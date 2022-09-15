from pytube import YouTube

# where to save
SAVE_PATH = "C:/Users/bsimb/Documents/Programmieren_Privat/Python/YT_mp4_downloader"  # to_do

# link of the video to be downloaded
link = ["https://www.youtube.com/watch?v=72axeq9Br4s", "https://www.youtube.com/watch?v=VtENVO5iaFs", "https://www.youtube.com/watch?v=C58GaCL7Bjk", "https://www.youtube.com/watch?v=kvwyR_eg9I8",
        "https://www.youtube.com/watch?v=LXCCPpm4_n0", "https://www.youtube.com/watch?v=Jz4zFQtN9HM", "https://www.youtube.com/watch?v=4Iw8X3eJ3ZU", "https://www.youtube.com/watch?v=K9h8DbgqeHY&t=814s",
        "https://www.youtube.com/watch?v=n0zonk7SSuw&t=68s"
        ]

for i in link:
    YouTube(i).streams.first().download(SAVE_PATH)
