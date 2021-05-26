import sys
m, n = list(map(int, sys.stdin.readline().split()))
board = []
start = []
for i in range(m):
    temp = list(map(int, sys.stdin.readline().strip()))
    board.append(temp)
    if i == 0:
        for j in range(len(temp)):
            if temp[j] == 1:
                start.append([0, j])


def DFS(board, m, n, start):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    while start:
        x, y = start.pop()
        for i in range(len(dx)):
            new_x, new_y = x+dx[i], y+dy[i]
            if 0 <= new_x < m and 0 <= new_y < n:
                if board[new_x][new_y] == 1:
                    if new_x == m-1:
                        print(1)
                        return
                    start.append([new_x, new_y])
                    board[new_x][new_y] = 0
    print(-1)
    return


DFS(board, m, n, start)
