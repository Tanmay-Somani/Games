import random

board = {
    "tl": "", "t": "", "tr": "",
    "ml": "", "m": "", "mr": "",
    "ll": "", "l": "", "lr": ""
}

def print_board(board):
    print(board["tl"] + " | " + board["t"] + " | " + board["tr"])
    print("- + - + -")
    print(board["ml"] + " | " + board["m"] + " | " + board["mr"])
    print("- + - + -")
    print(board["ll"] + " | " + board["l"] + " | " + board["lr"])


def choose_symbol():
    while True:
        choice = input("Enter whether you want X or O: ").upper()
        if choice == "X" or choice == "O":
            return choice
        else:
            print("Invalid choice, please choose again.")


def input_user(symbol):
    while True:
        entry = input("Enter the area you want to place it in (1-9): ")
        if entry in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = {
                "1": "tl", "2": "t", "3": "tr",
                "4": "ml", "5": "m", "6": "mr",
                "7": "ll", "8": "l", "9": "lr"
            }[entry]
            if board[position] == "":
                board[position] = symbol
                break
            else:
                print("That position is already occupied. Choose another.")
        else:
            print("Invalid input. Please enter a number between 1 and 9.")


def play_game():
    player_symbol = choose_symbol()
    computer_symbol = "X" if player_symbol == "O" else "O"
    
    print("You chose:", player_symbol)
    
    while True:
        print_board(board)
        input_user(player_symbol)
        print_board(board)
        comp_entry = random.choice([pos for pos in board.keys() if board[pos] == ""])
        board[comp_entry] = computer_symbol
        print_board(board)


play_game()
