import os
from creature import Creature

def display_menu():
    print("\nMythical Creature Family Tree")
    print("1. Add child to a creature")
    print("2. Print the tree")
    print("3. Search for a creature and display ancestors")
    print("4. Exit")

def main():
    root = None

    while True:
        if root is None:
            clear_screen()
            print("\nMythical Creature Family Tree")
            name = input("Enter the name of the root creature: ")
            root = Creature(name)
            print(f"Root creature '{name}' created!")

        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            parent_name = input("Enter the name of the parent creature: ")
            parent, _ = root.search(parent_name)
            if not parent:
                clear_screen(f"Creature '{parent_name}' not found.")
            elif parent.left_child and parent.right_child:
                clear_screen(f"Creature '{parent_name}' already has two children. Choose a different parent.")
            else:
                child_name = input("Enter the name of the new child creature: ")
                added = parent.add_child(child_name)
                if added:
                    clear_screen(f"Child '{child_name}' added to '{parent_name}'.")

        elif choice == "2":
            print("\nFamily Tree:")
            root.print_tree()

        elif choice == "3":
            name = input("Enter the name of the creature to search for: ")
            creature, ancestors = root.search(name)
            if creature:
                clear_screen(f"Creature '{name}' found. Ancestors: {', '.join(ancestors) if ancestors else 'None'}.")
            else:
                clear_screen(f"Creature '{name}' not found.")

        elif choice == "4":
            clear_screen("Exiting the program. Goodbye!")
            break

        else:
            clear_screen("Invalid choice. Please try again.")

def clear_screen(message = None):
    os.system('cls' if os.name == 'nt' else 'clear')
    if message:
        print(message)

if __name__ == "__main__":
    main()
