import sys
input = sys.stdin.readline
n = int(input())
board = [list(map(int, input().split())) for i in range(n)]
board.sort(key=lambda x: (x[0], x[1]))
result = 0
low = board[0][0]
high = board[0][1]

for i in range(1, len(board)):
    start, end = board[i][0], board[i][1]
    if start <= high and end > high:
        high = end
    elif start > high:
        result += high - low
        low, high = start, end
result += high - low
print(result)
