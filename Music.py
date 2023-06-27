import abc


class Song(abc.ABC):
    history = []

    def __init__(self, title: str, artist: str, length: str):
        self.title = title
        self.artist = artist
        self.length = length

    def listening(self):
        print(self.title, 'is listening')
        self.history.append(self.title)


class Album:
    def __init__(self, title: str, artist: str, date: str):
        self.title = title
        self.artist = artist
        self.date = date


class Playlist:
    def __init__(self, name: str):
        self.name = name
        self.songs = []

    def add_song(self, song: Song):
        if song in self.songs:
            print('Song already exists.')
        else:
            self.songs.append(song)

    def remove_song(self, song: Song):
        self.songs.remove(song)

    def display_playlist(self):
        for i in self.songs:
            print(pl1.name, '-', [i.title, i.artist, i.length])

    def search(self, song_name: str):
        for i in self.songs:
            if i.title == song_name:
                print(f'"{song_name}" song is present in "{self.name}" playlist. ')
                break
        else:
            print('Song not found!')

    def view_history(self):
        print('History - ', Song.history)


class Rock(Song):
    def __init__(self, title: str, artist: str, length: str):
        super().__init__(title, artist, length)


class Pop(Song):
    def __init__(self, title: str, artist: str, length: str):
        super().__init__(title, artist, length)


pl1 = Playlist('playlist1')
pl2 = Playlist('playlist2')
song1 = Song('name1', 'artist1', '3;10')
song2 = Song('name2', 'artist2', '3;10')
pl1.add_song(song1)
pl1.add_song(song2)
pl1.display_playlist()
pl1.search('name2')
song1.listening()
song2.listening()
song2.listening()
pl1.view_history()
del pl2
