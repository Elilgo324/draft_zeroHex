# script gets HEX game in letters like: W[aa];B[bb];W[cd];B[dd])
# prints the board in every step
import numpy as np
board_size = 11

def getNumeric(letter):
    return ord(letter) - 97

# open file of games. read one game
f = open("NEW1999CHANGED.txt", "r")
line = f.readline()
print(line)
# initialize board with 0's
Wboard = np.zeros((board_size, board_size))
Bboard = np.zeros((board_size, board_size))
board = [Wboard, Bboard]

# organize locations
sp_line = line.split(";")
locations = []
for loc in sp_line:
    x_val = getNumeric(loc[2])
    y_val = getNumeric(loc[3])
    location = [x_val, y_val]
    locations.append(location)
print(locations)

turn = "W"
# modify board
for locat in locations:
    print("its " + turn + " turn:")
    if turn == "W":
        board[0][locat[0], locat[1]] = 1
        turn = "B"
    else:
        board[1][locat[0], locat[1]] = 1
        turn = "W"
    print(board)




