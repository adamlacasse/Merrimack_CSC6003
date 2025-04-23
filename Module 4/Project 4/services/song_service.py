from models.song import Song

def add_song(user, title, artist, album):
    song = Song(title, artist, album)
    user.songs.append(song)

def delete_song(user, title):
    for song in user.songs:
        if song.title == title:
            user.songs.remove(song)
            return f'Song "{title}" has been deleted.'
    return f'Song "{title}" not found.'

def update_song(user, title, new_artist=None, new_album=None):
    for song in user.songs:
        if song.title == title:
            if new_artist:
                song.artist = new_artist
            if new_album:
                song.album = new_album
            return f'Song "{title}" has been updated.'
    return f'Song "{title}" not found.'

def get_song_details(user, title):
    for song in user.songs:
        if song.title == title:
            return vars(song)
    return f'Song "{title}" not found.'

def display_all_songs(user):
    if not user.songs:
        return 'No songs in the list.'
    return [vars(song) for song in user.songs]
