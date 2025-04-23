import random

def draw_board(board):
    print("  " + " ".join(str(i) for i in range(len(board))))
    for idx, row in enumerate(board):
        print(f"{idx} " + " ".join(row))

def place_ships(board, NUM_SHIPS):
    ship_locations = set()
    while len(ship_locations) < NUM_SHIPS:
        row = random.randint(0, len(board) - 1)
        col = random.randint(0, len(board) - 1)
        if (row, col) not in ship_locations:
            ship_locations.add((row, col))
            board[row][col] = "S"
    return ship_locations

def get_user_input():
    while True:
        try:
            row, col = map(int, input("Enter row and column number separated by a space (e.g., 3 4): ").split())
            if 0 <= row < 10 and 0 <= col < 10:
                return row, col
            else:
                print("Input is out of bounds. Try again.")
        except ValueError:
            print("Invalid input. Please enter two integers separated by a space.")

def main():
    NUM_SHIPS = 5
    board = [["." for _ in range(10)] for _ in range(10)]
    ships = place_ships(board, NUM_SHIPS)
    hits = 0

    print("Welcome to Battleship!")
    draw_board(board)

    while hits < NUM_SHIPS:
        row, col = get_user_input()
        if (row, col) in ships:
            print("Hit!")
            board[row][col] = "X"
            ships.remove((row, col))
            hits += 1
        elif board[row][col] == ".":
            print("Miss!")
            board[row][col] = "O"
        else:
            print("You already guessed that location.")
        
        draw_board(board)

    print("Congratulations! You sank all the ships!")

main()
