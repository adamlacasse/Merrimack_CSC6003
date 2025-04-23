def display_main_menu():
    print("Welcome to the Music Library App")
    print("Please choose an option:")
    print("1. Add user")
    print("2. Change user")
    print("3. Add a song")
    print("4. Get song details")
    print("5. Update song details")
    print("6. Delete a song")
    print("7. Display all songs")
    print("8. Exit")

def get_user_choice():
    choice = input("Enter your choice (1-8): ")
    return choice.strip()
