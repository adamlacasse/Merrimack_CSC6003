import random

def main():
    # Step 1: Generate a random number between 1 and 100
    random_number = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I have generated a random number between 1 and 100. Can you guess it?")

    while True:
        try:
            # Step 2: Ask the user to guess the number
            guess = int(input("Enter your guess: "))
            attempts += 1

            # User isn't following instructions, lol
            if guess > 100 or guess < 1:
                print("Please enter a number between 1 and 100.")

            elif guess == random_number:
                # Step 2b.i: Congratulate the user and end the program
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break
            elif guess < random_number:
                print("Too low!")
            else:
                print("Too high!")

            # Step 2a.ii: Provide a hint after the second incorrect guess
            if attempts == 2:
                print("Here's a hint:")
                hint = random.choice([
                    f"The number is {'even' if random_number % 2 == 0 else 'odd'}.",
                    f"The number is a multiple of 5." if random_number % 5 == 0 else "The number is not a multiple of 5.",
                    f"The number squared is {'greater' if random_number ** 2 > 1000 else 'less'} than 1,000."
                ])
                print(hint)

        # User STILL isn't following instructions!
        except ValueError:
            print("Please enter a valid number.")
main()
