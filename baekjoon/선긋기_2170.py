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

# 택이코드
# import sys

# n = int(sys.stdin.readline().strip())
# points = [[int(x) for x in sys.stdin.readline().split()] for _ in range(n)]
# points.sort(key = lambda x: (x[0], x[1]))
# start, end = points[0][0], points[0][1]
# result, temp = 0, end-start

# for i in range(n-1):
#     # x1, y1 = points[i]
#     x2, y2 = points[i+1]
#     if end >= x2 and y2 > end:
#         # start, end = min(start, x1), max(end, y1, y2)
#         start, end = start, y2
#     # else:
#     elif end < x2:
#         # result += temp
#         result += end - start
#         start, end = x2, y2
#     # temp = end-start
# result += end - start
# # if temp != 0:
# #     result += temp

# print(result)