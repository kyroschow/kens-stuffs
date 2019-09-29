size = 9
rowSize = 3
steps = 4
board = [["1", "2", "3"],
         ["4", "5", "6"],
         ["7", "8", "9"]]


def print_board(board):
    for row in board:
        print("".join(row))


for step in range(steps):
    print_board(board)
    if step % 2 == 0:
        location = int(input("x: ")) - 1
        board[int(location / rowSize)][location % rowSize] = "x"
    else:
        location = int(input("o: ")) - 1
        board[int(location / rowSize)][location % rowSize] = "o"
print_board(board)