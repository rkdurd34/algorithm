import sys

n = int(sys.stdin.readline())
board = [[], []]
board[0].append([0]+list(map(int, sys.stdin.readline().split()))+[0])
board[0].append([0]+list(map(int, sys.stdin.readline().split()))+[0])
board[1].append([0]+list(map(int, sys.stdin.readline().split()))+[0])
board[1].append([0]+list(map(int, sys.stdin.readline().split()))+[0])

a, b = board[0][0][0], board[0][1][0]
print(board)
for i in range(n+1):
    print(a, b)
    temp_a = a
    temp_b = b
    a = min(temp_a + board[0][0][i+1], temp_b +
            board[0][1][i+1] + board[1][1][i+1])
    b = min(temp_b + board[0][1][i+1], temp_a +
            board[0][0][i+1] + board[1][0][i+1])


print(a, b)
