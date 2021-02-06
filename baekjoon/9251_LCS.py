import sys
a = sys.stdin.readline().strip()
b = sys.stdin.readline().strip()
board = [[0 for _ in range(len(b)+1)] for _ in range(len(a)+1)]
for i in range(len(a)):
    for j in range(len(b)):
        if a[i] == b[j]:
            board[i+1][j+1] = 1 + board[i][j]
        else:
            board[i+1][j+1] = max(board[i][j+1], board[i+1][j])
print(board[-1][-1])
# print(board)
