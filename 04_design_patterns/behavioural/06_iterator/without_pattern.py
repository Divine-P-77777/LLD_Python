class Song:
    def __init__(self, title: str):
        self._title = title

    def get_title(self):
        return self._title


class Playlist:
    def __init__(self):
        self._playlist = []

    def add_song(self, song: Song):
        self._playlist.append(song)

    def get_playlist(self):
        return self._playlist


# Client
playlist = Playlist()
playlist.add_song(Song("Song 1"))
playlist.add_song(Song("Song 2"))

for i in range(len(playlist.get_playlist())):
    print(playlist.get_playlist()[i].get_title())