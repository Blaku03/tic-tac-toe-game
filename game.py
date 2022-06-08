import os

# clearing console
def clear():
    return os.system("cls")


# game
def game():

    # sides
    print("Now let's choose player's one side!")
    player1_side = choose_side()

    if player1_side == "X":
        player2_side = "O"
    else:
        player2_side = "X"

    values_board = [
        "",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
    ]

    round = 0

    what_player = player1_side

    while round < 9 and winning_con(values_board):

        display_board(values_board)

        cell = valid_board_number(values_board)
        round += 1

        clear()

        if what_player == player1_side:
            values_board[cell] = player1_side
            what_player = player2_side
            winner = player1_side
        else:
            values_board[cell] = player2_side
            what_player = player1_side
            winner = player2_side

    # end of the game message
    clear()

    if winning_con(values_board) == False:
        print(f"{winner} have won the game!")

    else:
        print("It's a draw!")


# display numbers corresponding to cell in play grid
def introduction():

    clear()
    print("Welcome to the Tic tac toe game!")

    introduction_board = ["", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    start = input("Are you ready to start the game ?: (Y or N): ")

    if start == "N":
        print("Okay then bye :(")
        exit()

    clear()
    print("Great!\nGrid is represented by numbers as follows: ")

    display_board(introduction_board)

    temp = input("Press anything to continue: ")
    clear()


def winning_con(board):

    nobody_won = True

    # row check
    for i in range(1, 8, 3):

        if board[i] == board[i + 1] == board[i + 2]:
            if board[i] == "X" or board[i] == "O":
                nobody_won = False

    #  column check
    for i in range(1, 4):

        if board[i] == board[i + 3] == board[i + 6]:
            if board[i] == "X" or board[i] == "O":
                nobody_won = False

    # diagonal check
    if board[1] == board[5] == board[9] or board[3] == board[5] == board[7]:
        if board[5] == "X" or board[5] == "O":
            nobody_won = False

    return nobody_won


def valid_board_number(board):

    try:
        cell = int(input("Choose a cell from 1 to 9: "))

        while cell not in range(1, 10):

            cell = int(input("Please eneter a valid number: "))

    except:
        cell = int(input("Please enter a number in base 10: "))

        while cell not in range(1, 10):

            cell = int(input("Please eneter a valid number: "))

    while board[cell] != " ":
        cell = int(input("This cell is already selected choose diffrent tile: "))

    return cell


def display_board(board):

    print(board[1] + "|" + board[2] + "|" + board[3])
    print(board[4] + "|" + board[5] + "|" + board[6])
    print(board[7] + "|" + board[8] + "|" + board[9])


def choose_side():

    player_input = input("Player 1 please choose X or O: ")

    while player_input != "X" and player_input != "O":

        print(f"There isn't side like {player_input}")
        player_input = input("Choose this time X or O: ")

    clear()
    return player_input


introduction()
game()
