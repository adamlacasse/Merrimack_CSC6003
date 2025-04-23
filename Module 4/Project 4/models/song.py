class Song:
    def __init__(self, title, artist, album):
        self.title = title
        self.artist = artist
        self.album = album

    def get_details(self):
        return {
            "title": self.title,
            "artist": self.artist,
            "album": self.album
        }
