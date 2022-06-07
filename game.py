import os

def display_board():

    #clear console
    clear = lambda: os.system('cls')
    clear()

    column = "\t\t\t|\t|\t"
    row = "\t\t__________________________"

    print(column)
    print(column)
    print(column)
    print(row)
    print(column)
    print(column)
    print(column)
    print(row)
    print(column)
    print(column)
    print(column)



