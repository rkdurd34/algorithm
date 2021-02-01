import sys
row = int(sys.stdin.readline())
board = []
check = []
for i in range(row):
    board.append(list(map(int, sys.stdin.readline().split())))
    check.append([0] * row)

check[0][0] = 1

for i in range(len(board)):
    for j in range(len(board[i])):
        if i == row-1 and j == row-1:
            continue
        if [i, j] != 0:
            dx = [board[i][j], 0]
            dy = [0, board[i][j]]
            for k in range(2):
                newX = i + dx[k]
                newY = j + dy[k]
                if 0 <= newX < len(board) and 0 <= newY < len(board):
                    check[newX][newY] += check[i][j]
print(check[-1][-1])
# import sys
# row = int(sys.stdin.readline())
# board = []
# check = []
# for i in range(row):
#     board.append(list(map(int, sys.stdin.readline().split())))
#     check.append([0] * row)

# check[0][0] = 1
# stack = [[0, 0]]
# count = 0
# while stack:
#     print(check)
#     temp_list = []
#     for temp in stack:
#         prevX = temp[0]
#         prevY = temp[1]
#         dx = [board[prevX][prevY], 0]
#         dy = [0, board[prevX][prevY]]
#         for i in range(2):
#             newX = prevX + dx[i]
#             newY = prevY + dy[i]
#             if 0 <= newX < len(board) and 0 <= newY < len(board):
#                 if board[newX][newY] == 0:
#                     count += check[prevX][prevY]
#                 elif check[newX][newY] == 0:
#                     check[newX][newY] = 1
#                     temp_list.append([newX, newY])
#                 elif check[newX][newY] != 0:
#                     check[newX][newY] += check[prevX][prevY]
#     stack = list(temp_list)
# print(count)
# import sys
# row = int(sys.stdin.readline())
# board = []

# for i in range(row):
#     board.append(list(map(int, sys.stdin.readline().split())))

# count = 0
# stack = [[0, 0]]
# while stack:
#     temp = stack.pop()
#     x = [board[temp[0]][temp[1]], 0]
#     y = [0, board[temp[0]][temp[1]]]
#     for i in range(2):
#         dx = temp[0] + x[i]
#         dy = temp[1] + y[i]
#         if 0 <= dx < len(board) and 0 <= dy < len(board):
#             if board[dx][dy] == 0:
#                 count += 1
#             else:
#                 stack.append([dx, dy])

# print(count)
