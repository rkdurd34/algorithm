import sys
row, col = list(map(int, sys.stdin.readline().split()))
r, c, dir = list(map(int, sys.stdin.readline().split()))
board = []
for i in range(row):
    board.append(list(map(int, sys.stdin.readline().split())))
need_visit = [r, c]
count = 1


def sol_0(dir, board, temp):
    global count
    prevx, prevy = temp[0], temp[1]
    dx = [0, 1, 0, -1, -1, 0, 1, 0, 0, -1, 0, 1, 1, 0, -1, 0]
    dy = [-1, 0, 1, 0, 0, -1, 0, 1, 1, 0, -1, 0, 0, 1, 0, -1]
    di = [3, 2, 1, 0, 0, 3, 2, 1, 1, 0, 3, 2, 2, 1, 0, 3]
    for i in range(4 * dir, 4 * dir + 4):
        x = temp[0] + dx[i]
        y = temp[1] + dy[i]
        if 0 <= x < row and 0 <= y < col:
            if board[x][y] == 0:
                need_visit = [x, y]
                count += 1
                dir = di[i]
                return [x, y], dir
    if board[prevx + dx[4 * dir + 1]][prevy + dy[4 * dir + 1]] == 1:
        return False, dir
    else:
        return [temp[0] + dx[4 * dir + 1], temp[1] + dy[4 * dir + 1]], dir


while need_visit:
    board[need_visit[0]][need_visit[1]] = 2
    need_visit, dir = sol_0(dir, board, need_visit)
print(count)
