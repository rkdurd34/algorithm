import sys
row = int(sys.stdin.readline())
board = []
check = []
for i in range(row):
    board.append(list(map(int, sys.stdin.readline().split())))
    check.append([{0: 0, 1: 0, 2: 0} for _ in range(row)])

check[0][1][0] = 1


def com_check(board, check, temp, stat):
    dx = [0, 1, 1]
    dy = [1, 0, 1]
    for i in range(3):
        x = temp[0] + dx[i]
        y = temp[1] + dy[i]
        if 0 <= x < len(board) and 0 <= y < len(board):
            if board[x][y] == 1:
                return False
        else:
            return False
    if 0 <= temp[0]+1 < len(board) and 0 <= temp[1]+1 < len(board):
        check[temp[0]+1][temp[1]+1][2] += check[temp[0]][temp[1]][stat]


def ind_check(board, check, temp, stat):
    dx = [0, 1, 1]
    dy = [1, 0, 1]
    if stat == 2:
        for i in range(2):
            x = temp[0] + dx[i]
            y = temp[1] + dy[i]
            if 0 <= x < len(board) and 0 <= y < len(board):
                if board[x][y] == 0:
                    check[x][y][i] += check[temp[0]][temp[1]][stat]

    elif stat == 1 or stat == 0:
        x = temp[0] + dx[stat]
        y = temp[1] + dy[stat]
        if 0 <= x < len(board) and 0 <= y < len(board):
            if board[x][y] == 0:
                check[x][y][stat] += check[temp[0]][temp[1]][stat]


# 가로 : 0, 세로: 1, 대각: 2
# 항상 생각해두기 bfs같은 문제더라도 왔던 길 돌아가지 않으면 DP로 풀 수 있음

for i in range(row):
    for j in range(row):
        for k in check[i][j]:
            if check[i][j][k] != 0:
                com_check(board, check, [i, j], k)
                ind_check(board, check, [i, j], k)
print(sum(check[-1][-1].values()))

# def sol(board, stat, temp):
#     global count
#     temp_list = []
#     dx = [0, 1, 1]
#     dy = [1, 0, 1]
#     prevx = temp[0]
#     prevy = temp[1]
#     for i in range(3):
#         x = prevx + dx[i]
#         y = prevy + dy[i]
#         if
#     return

# count = 0
# stack = [[0, 1, 0]]
# while stack:
#     temp = stack.pop()
#     loc = temp[:2]
#     stat = temp[2]
#     stack.extend(sol(board, stat, temp))
