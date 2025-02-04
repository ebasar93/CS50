"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    return 'X' if sum([row.count('X') for row in board]) == sum([row.count('O') for row in board]) else 'O'


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    a = set()
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell == EMPTY:
                a.add((i,j))
    return a


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # check the action is valid
    i,j = action
    new_board = copy.deepcopy(board)
    if new_board[i][j] != EMPTY:
        raise "invalid move"

    else:
        if player(new_board) == "X":
            new_board[i][j] = "X"
            return new_board
        else:
            new_board[i][j] = "O"
            return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    #check horizontal
    if max([row.count("X") for row in board]) == 3:
        return "X"
    elif max([row.count("O") for row in board]) == 3:
        return "O"
    #check diagonal
    if board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0]:
        if board[1][1] == "X":
            return "X"
        elif board[1][1] == "O":
            return "O"
        else:
            return None
    #check vertical
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i]:
            if board[0][i] == "X":
                return "X"
            elif board[0][i] == "O":
                return "O"
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == "X" or winner(board) == "O":
        return True
    for row in board:
        if row.count(EMPTY) > 0:
            return False
    return True

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == "X" :
        return 1
    elif  winner(board) == "O":
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # Max value state
    if player(board) == "X":
        value = -math.inf
        for action in actions(board):
            new_value = min_value(result(board,action))
            if new_value > value:
                value = new_value
                best_action = action
        return best_action

    # Min value state
    else:
        value = math.inf
        for action in actions(board):
            new_value = max_value(result(board,action))
            if new_value < value:
                value = new_value
                best_action = action
        return best_action

def max_value(board):
    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v

def min_value(board):
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v



