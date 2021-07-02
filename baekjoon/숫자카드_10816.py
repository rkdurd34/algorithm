import sys
from collections import defaultdict
board = defaultdict(int)
input = sys.stdin.readline
n = int(input())
# board = list(map(int, input().split()))
for i in input().split():
    board[int(i)] += 1
# print(board)
m = int(input())
# check = list(map(int, input().split()))
result = []
for i in input().split():
    temp = int(i)
    result.append(board[temp])
# board.sort()
print(*result)
