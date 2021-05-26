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


def BFS(board, m, n, start):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    count = 1
    while start:
        temp_list = []
        for temp in start:
            x, y = temp
            for i in range(len(dx)):
                new_x, new_y = x+dx[i], y+dy[i]
                if 0 <= new_x < m and 0 <= new_y < n:
                    if board[new_x][new_y] == 1:
                        if new_x == m-1:
                            print(count+1)
                            return
                        temp_list.append([new_x, new_y])
                        board[new_x][new_y] = 0
        count += 1
        start = temp_list
    print(-1)
    return


BFS(board, m, n, start)
