import sys
col, row, height = list(map(int, sys.stdin.readline().split()))
board = []
check = []
stack = []
for i in range(height):
    temp_list = []
    temp_check_list = []
    for j in range(row):
        row_temp = []
        s = sys.stdin.readline().split()
        for k in range(len(s)):
            row_temp.append(int(s[k]))
            if s[k] == "1":
                stack.append([j, k, i])
            # temp_list.append(list(map(int, sys.stdin.readline().split())))
            # temp_check_list.append([False] * col)
        temp_list.append(row_temp)
    board.append(temp_list)
    check.append(temp_check_list)
# print(board)
# print(stack)


def bfs(board, check, stack, count):

    dx = [0, 0, 1, -1, 0, 0]
    dy = [1, -1, 0, 0, 0, 0]
    dz = [0, 0, 0, 0, 1, -1]
    while stack:
        temp_list = []
        for temp in stack:
            for i in range(6):
                x = temp[0] + dx[i]
                y = temp[1] + dy[i]
                z = temp[2] + dz[i]
                if 0 <= x < len(board[0]) and 0 <= y < len(board[0][0]) and 0 <= z < len(board):
                    if board[z][x][y] == 0:
                        temp_list.append([x, y, z])
                        board[z][x][y] = 1
        stack = list(temp_list)
        count += 1
        # check[z][x][y] = True
    return count


def check(result):
    for i in board:
        for j in i:
            if 0 in j:
                result = -1
                return result
    return result


result = bfs(board, check, stack, -1)
a = check(result)
print(a)
