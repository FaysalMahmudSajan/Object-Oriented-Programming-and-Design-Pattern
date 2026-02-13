class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)
        print(f"Added: {song}")

    def remove_song(self, song):
        if song in self.songs:
            self.songs.remove(song)
            print(f"Removed !")
        else:
            print("It's not exist")

    def show_songs(self):
        print(self.songs)


my_playlist = Playlist("Liked")
my_playlist.show_songs()
my_playlist.add_song("Eta")
my_playlist.add_song("Valo basher golpo")
my_playlist.add_song("rat ghum")
my_playlist.add_song("Eta")


my_playlist.show_songs()

my_playlist.remove_song("Eta")
my_playlist.remove_song("Eta")

my_playlist.show_songs()

my_playlist.remove_song("Eta")
