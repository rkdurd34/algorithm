import sys
row, col, rec = list(map(int, sys.stdin.readline().split()))
board = [[0 for _ in range(col)] for _ in range(row)]
for i in range(rec):
    x1, y1, x2, y2 = list(map(int, sys.stdin.readline().split()))
    left = [x1, y1]
    right = [x2-1, y2-1]  # 0 2, 3 3
    for i in range(left[1], right[1]+1):
        for j in range(left[0], right[0]+1):
            if board[i][j] == 0:
                board[i][j] = 1

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
count = 0
count_result = []
for i in range(len(board)):
    for j in range(len(board[0])):
        stack = []
        temp_count = 1
        if board[i][j] == 0:
            stack.append([i, j])
            board[i][j] = 1
            while stack:
                temp = stack.pop()
                for a in range(4):
                    x = temp[0] + dx[a]
                    y = temp[1] + dy[a]
                    if 0 <= x < len(board) and 0 <= y < len(board[0]) and board[x][y] == 0:
                        temp_count += 1
                        stack.append([x, y])
                        board[x][y] = 1
            count_result.append(temp_count)
            count += 1
# print(board)
print(count)
print(*sorted(count_result))
# if len(count_result) == 0:
#     print(row*col)
# else:
#     print(*sorted(count_result))
