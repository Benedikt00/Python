
import lyricsgenius as lg
import settings
from mutagen.id3 import ID3, TIT2, TPE1

genius = lg.Genius(settings.client_accesstoken, skip_non_songs=True, excluded_terms=["(Remix)", "(Live)"], remove_section_headers=True)


def get_lyrics(artist, name):
    try:
        song = genius.search_song(name, artist)
        print(song.lyrics)
    except Exception as e:
        print(f"some exception at {name}: {e}")


if __name__ == '__main__':
    get_lyrics("Lena", "Satellite")