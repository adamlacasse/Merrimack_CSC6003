import os

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        return "I don't know my sound"

    def info(self):
        return f"{self.name} is a {self.species} and makes a {self.make_sound()} sound."

class Bear(Animal):
    def __init__(self, name, species, fur_color):
        super().__init__(name, species)
        self.fur_color = fur_color

    def make_sound(self):
        return "roar"

    def info(self):
        return f"{self.name} is a {self.species} with {self.fur_color} fur that makes a {self.make_sound()} sound."

class Elephant(Animal):
    def __init__(self, name, species, weight):
        super().__init__(name, species)
        self.weight = weight

    def make_sound(self):
        return "trumpet"

    def info(self):
        return f"{self.name} is a {self.species} weighing {self.weight} kg that makes a {self.make_sound()} sound."

class Penguin(Animal):
    def __init__(self, name, species, height):
        super().__init__(name, species)
        self.height = height

    def make_sound(self):
        return "squawk"

    def info(self):
        return f"{self.name} is a {self.species} standing at {self.height} ft that makes a {self.make_sound()} sound."

def zoo_menu():
    clear_screen()
    zoo = []

    while True:
        print("===Zoo Menu===")
        print("1) Add an animal to the zoo")
        print("2) Print all animals in the zoo")
        print("3) Print all animals of a species")
        print("4) Clear the screen")
        print("5) exit\n")
        choice = input("Your choice: ")

        if choice == "1":
            print("===Add Menu===")
            print("1) Add a bear")
            print("2) Add an elephant")
            print("3) Add a penguin")
            print("\n")
            add_choice = input("Your choice: ")

            if add_choice == "1":
                name = input("Input name: ")
                species = "bear"
                fur_color = input("Input fur color: ")
                zoo.append(Bear(name, species, fur_color))

            elif add_choice == "2":
                name = input("Input name: ")
                species = "elephant"
                weight = float(input("Input weight (in kg): "))
                zoo.append(Elephant(name, species, weight))

            elif add_choice == "3":
                name = input("Input name: ")
                species = "penguin"
                height = float(input("Input height (in ft): "))
                zoo.append(Penguin(name, species, height))

        elif choice == "2":
            for animal in zoo:
                print(animal.info())

        elif choice == "3":
            print("===Print Species Menu===")
            print("1) Print all the bears")
            print("2) Print all the elephants")
            print("3) Print all the penguins")
            print("=============")
            print_choice = input("Your choice: ")

            if print_choice == "1":
                for animal in zoo:
                    if isinstance(animal, Bear):
                        print(animal.info())

            elif print_choice == "2":
                for animal in zoo:
                    if isinstance(animal, Elephant):
                        print(animal.info())

            elif print_choice == "3":
                for animal in zoo:
                    if isinstance(animal, Penguin):
                        print(animal.info())

        elif choice == "4":
            clear_screen()
        
        elif choice == "5":
            break

        else:
            print("Invalid choice. Please try again.")

# Clears the terminal screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    zoo_menu()
