from abc import ABC, abstractmethod
from typing import List


class Song:
    def __init__(self, title: str):
        self._title = title

    def get_title(self):
        return self._title


# Iterator Interface
class Iterator(ABC):
    @abstractmethod
    def has_next(self) -> bool:
        pass

    @abstractmethod
    def next(self) -> Song:
        pass


# Concrete Iterator
class PlaylistIterator(Iterator):
    def __init__(self, songs: List[Song]):
        self._songs = songs
        self._position = 0

    def has_next(self) -> bool:
        return self._position < len(self._songs)

    def next(self) -> Song | None:
        while self.has_next() == True:
            song = self._songs[self._position]
            self._position += 1
            return song
        return None


# Collection
class Playlist:
    def __init__(self):
        self._songs: List[Song] = []

    def add_song(self, song: Song):
        self._songs.append(song)

    def create_iterator(self) -> Iterator:
        return PlaylistIterator(self._songs)


# Client
playlist = Playlist()

playlist.add_song(Song("Song 1"))
playlist.add_song(Song("Song 2"))
playlist.add_song(Song("Song 3"))
playlist.add_song(Song("Song 4"))

iterator = playlist.create_iterator()

while iterator.has_next():
    print(iterator.next().get_title())