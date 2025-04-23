class User:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def delete_song(self, title):
        for song in self.songs:
            if song.title == title:
                self.songs.remove(song)
                return True
        return False

    def get_song_details(self, title):
        for song in self.songs:
            if song.title == title:
                return song
        return None

    def update_song(self, title, new_song):
        for index, song in enumerate(self.songs):
            if song.title == title:
                self.songs[index] = new_song
                return True
        return False

    def display_songs(self):
        return self.songs if self.songs else "No songs available."
