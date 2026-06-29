import tictactoe as ttt

X = "X"
O = "O"
EMPTY = None

board = [[X, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY]]
print(board)
print(ttt.player(board))

action = ttt.actions(board)
for i in action:
    print(i)
print(action)