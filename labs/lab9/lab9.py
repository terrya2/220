"""
Autumn Terry
lab9.py
Create a program with while loops and boolean logic.
I certify that this assignment is my own work, but I discussed it with: Brooke Duvall
"""

def tic_tac_toe():
    board = build_board()
    new_game = True
    while new_game:
        play(board)
        new = input("do you want to play again")
        if new.startswith("y"):
            board = build_board()
            new_game = True
        else:
            new_game = False

def build_board():
    board_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return board_nums
def fill_spot(board, position, shape):
    board[position - 1] =shape
def is_legal(board, position):
    if str(board[position - 1]).isnumeric():
        return True
    return False
def game_is_won(board):
    for i in range(3):
        if board[i] == board[i +3] and board[i] == board[i +6]:
            return True
    for i in range(3):
        if board[i * 3] == board[(i * 3) +1] and board[i * 3] == board[(i * 3) +2]:
            return True
    if board[0] == board[4] and board[4] == board[8]:
        return True
    if board[2] == board[4] and board[4] == board[6]:
        return True
    return False

def game_over(board):
    if game_is_won(board):
        return True
    non_numer = 0
    for i in board:
        if not str(i).isnumeric():
            non_numer += 1
    if non_numer == 9:
        return True
    return False
def get_winner(board):
    if not game_is_won(board):
        return "None"
    for i in range(3):
        if board[i] == board[i +3] and board[i] == board[i +6] and board[i] == "x":
            return "x"
        if board[i] == board[i +3] and board[i] == board[i +6] and board[i] == "o":
            return "o"
    for i in range(3):
        if board[i * 3] == board[(i * 3) +1] and board[i * 3] == board[(i * 3) +2] and board[i] == "x":
            return "x"
        if board[i * 3] == board[(i * 3) +1] and board[i * 3] == board[(i * 3) +2] and board[i] == "o":
            return "o"
    if board[0] == board[4] and board[4] == board[8] and board[0] == "x":
        return "x"
    if board[0] == board[4] and board[4] == board[8] and board[0] == "o":
        return "o"
    if board[2] == board[4] and board[4] == board[6] and board[2] == "x":
        return "x"
    if board[2] == board[4] and board[4] == board[6] and board[2] == "o":
        return "o"
def play(board):
    is_x_turn = True
    while not game_is_won(board):
        print_board(board)
        if is_x_turn:
            position = eval(input("x's choose a position: "))
        else:
            position = eval(input("o's choose a position: "))
        if is_legal(board, position):
            if is_x_turn:
                fill_spot(board, position, "x")
            else:
                fill_spot(board, position, "o")
            is_x_turn = not is_x_turn

    winner = get_winner(board)
    if winner == "x":
        print("x's win")
    if winner == "0":
        print("o's win")
    if winner == "none":
        print("Tie")




def print_board(board):
    """ prints the values of board """
    RED = "\033[1;31m"
    BLUE = "\033[1;36m"
    LIGHT_GRAY = "\033[0;37m"
    reset = "\033[0m"
    new_board = []
    for v in board:
        new_board.append(v)
    for i in range(len(board)):
        if str(board[i]).find('x') >= 0:
            new_board[i] = RED + board[i] + LIGHT_GRAY
        elif str(board[i]).find('o') >= 0:
            new_board[i] = BLUE + board[i] + LIGHT_GRAY
    row_format = ' {0} | {1} | {2} '
    row_1 = row_format.format(new_board[0], new_board[1], new_board[2])
    row_2 = row_format.format(new_board[3], new_board[4], new_board[5])
    row_3 = row_format.format(new_board[6], new_board[7], new_board[8])
    row_separator = '-' * 11
    print(LIGHT_GRAY)
    print(row_1)
    print(row_separator)
    print(row_2)
    print(row_separator)
    print(row_3)
    print(reset)