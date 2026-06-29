"""
Tic Tac Toe Player
"""

import math,copy

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
    count_X = sum(row.count(X) for row in board)
    
    count_O = sum(row.count(O) for row in board)
    
    if count_X > count_O:
        return O
    else:
        return X 
    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    action_set = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] is None:
                action_set.add((i,j))
    return action_set


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    if action not in actions(board):
        raise ValueError
    copy_board = copy.deepcopy(board)   
    i,j = action
    player_moves = player(board)

    copy_board[i][j] =  player_moves 

    return copy_board
    


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    
    # check rows
    for i in range(3):
        if board[i][0] != EMPTY and board[i][0] == board[i][1] == board[i][2]:
            return board[i][0]
    
    # check column
    for j in range(3):
        if board[0][j] != EMPTY and board[0][j] == board[1][j] == board[2][j]:
            return board[0][j]
    
    # check diagonals
    if board[0][0] != EMPTY and board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] != EMPTY and board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]
    return None

    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == X or winner(board) == O:
        return True

    count_EMPTY = sum(row.count(EMPTY) for row in board)

    if count_EMPTY == 0:
        return True
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    if winner(board) == O:
        return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    
    if terminal(board) == True:
        return None
    player_moves = player(board)
    best_move = None
    # MAX
    if player_moves == X:
        best_score = float('-inf')
        for i in actions(board):
            new_board = result(board,i)
            score = value(new_board)
            if score > best_score:
                best_score = score
                best_move = i
    # MIN
    if player_moves == O:
        best_score = float('inf')
        for i in actions(board):
            new_board = result(board,i)
            score = value(new_board)
            if score < best_score:
                best_score = score
                best_move = i
    return best_move

def value(board):
    if terminal(board) == True:
        return utility(board)
    player_moves = player(board)
    
    if player_moves == X:
        best_score = float('-inf')
        for i in actions(board):
            
            best_score = max(best_score,value(result(board,i)))
        return best_score
            
    if player_moves == O:
        best_score = float('inf')
        for i in actions(board):
            
            best_score = min(best_score,value(result(board,i)))
            
        return best_score
    raise NotImplementedError
