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
    print("Great grid is represented by numbers like this:")

    display_board(introduction_board)

    temp = input("Press anything to continue: ")
    clear()


def winning_con():
    pass


def valid_board_number():
    pass


# TODO funconial board
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


# game
introduction()

# player1_side = choose_side()
# round = 0
# player1_turn = True
# player_pick = None

# values_board = [
#     " ",
#     " ",
#     " ",
#     " ",
#     " ",
#     " ",
#     " ",
#     " ",
#     " ",
#     " ",
# ]

# while round < 9:

#     if player1_turn:

#         player_pick = int(input("Choose number from 1 to 9: "))
#         clear()
#         values_board[player_pick] = player1_side
#         player1_turn = False

#     else:

#         player_pick = int(input("Choose number from 1 to 9: "))
#         clear()
#         values_board[player_pick] = player2_side
#         player1_turn = True

#     display_board(values_board)

#     round += 1
