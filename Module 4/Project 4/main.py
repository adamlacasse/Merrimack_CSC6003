from services.user_service import add_user, change_user, get_user
from services.song_service import add_song, delete_song, update_song, get_song_details, display_all_songs

class MusicLibraryApp:
    def __init__(self):
        # This variable keeps track of the user who is currently logged in
        self.current_user = None

    def main_menu(self):
        while True:
            print("\nMain Menu:")
            print("1. Add user")
            print("2. Change user")
            print("3. Add a song")
            print("4. Get song details")
            print("5. Update song details")
            print("6. Delete a song")
            print("7. Display all songs")
            print("8. Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                self.add_user()
            elif choice == '2':
                self.change_user()
            elif choice == '3':
                self.add_song()
            elif choice == '4':
                self.get_song_details()
            elif choice == '5':
                self.update_song_details()
            elif choice == '6':
                self.delete_song()
            elif choice == '7':
                self.display_all_songs()
            elif choice == '8':
                print("Exiting the application.")
                break
            else:
                print("Invalid choice. Please try again.")

    def add_user(self):
        name = input("Enter your name: ")
        print(add_user(name))
        self.current_user = get_user(name)

    def change_user(self):
        name = input("Enter user name to switch: ")
        self.current_user = get_user(name)
        print(change_user(name))

    def add_song(self):
        if self.current_user:
            title = input("Enter song title: ")
            artist = input("Enter artist name: ")
            album = input("Enter album name: ")
            add_song(self.current_user, title, artist, album)
            print(f"Song '{title}' added to {self.current_user.name}'s library.")
        else:
            print("Please log in to add a song.")

    def get_song_details(self):
        if self.current_user:
            title = input("Enter song title to get details: ")
            print(get_song_details(self.current_user, title))
        else:
            print("Please log in to get song details.")

    def update_song_details(self):
        if self.current_user:
            title = input("Enter song title to update: ")
            new_artist = input("Enter new artist name (leave blank to skip): ")
            new_album = input("Enter new album name (leave blank to skip): ")
            print(update_song(self.current_user, title, new_artist, new_album))
        else:
            print("Please log in to update song details.")

    def delete_song(self):
        if self.current_user:
            title = input("Enter song title to delete: ")
            print(delete_song(self.current_user, title))
        else:
            print("Please log in to delete a song.")

    def display_all_songs(self):
        if self.current_user:
            print(display_all_songs(self.current_user))
        else:
            print("Please log in to display songs.")

if __name__ == "__main__":
    app = MusicLibraryApp()
    app.main_menu()
