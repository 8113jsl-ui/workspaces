board = []

for i in range(19):
    board.append(list(map(int, input().split())))

n = int(input())

for i in range(n):
    x, y = map(int, input().split())

    for j in range(19):
        if board[x-1][j] == 0:
            board[x-1][j] = 1
        else:
            board[x-1][j] = 0

        if board[j][y-1] == 0:
            board[j][y-1] = 1
        else:
            board[j][y-1] = 0

for i in range(19):
    for j in range(19):
        print(board[i][j], end=" ")
    print()
