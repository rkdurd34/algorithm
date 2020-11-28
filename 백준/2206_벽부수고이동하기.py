import sys
sys.setrecursionlimit(999999999)
row, col = list(map(int, sys.stdin.readline().split()))
board = []
for i in range(row+2):
  if i == 0 or i == row + 1:
    board.append([float('inf') for _ in range(col+2)])
  else:
    board.append([float('inf')] + list(map(int,(list(sys.stdin.readline().strip()))))+ [float('inf')])
answer = float('inf')
board[1][1] = True
# print(board)
def DFS(distance, board, index):
    # print(index)
    global answer
    if index[:2] == [row,col]:
        if answer > distance:
            answer = distance
        return
    else:
        x = index[0]
        y = index[1]
        z = index[2]
        if board[x+1][y] == 0:
            board[x+1][y] = float('inf')
            DFS(distance+1, board, [x+1,y,z])
            board[x+1][y] = 0
        if board[x+1][y] ==1 and z  == 0:
            board[x+1][y] = float('inf')
            DFS(distance+1, board, [x+1,y,1])
            board[x+1][y] = 1
        if board[x-1][y] == 0:
            board[x-1][y] = float('inf')
            DFS(distance+1, board, [x-1,y,z])
            board[x-1][y] = 0
        if board[x-1][y] ==1 and z  == 0:
            board[x-1][y] = float('inf')
            DFS(distance+1, board, [x-1,y,1])
            board[x-1][y] = 1
        if board[x][y+1] == 0:
            board[x][y+1] = float('inf')
            DFS(distance+1, board, [x,y+1,z])
            board[x][y+1] = 0
        if board[x][y+1] ==1 and z  == 0:
            board[x][y+1] = float('inf')
            DFS(distance+1, board, [x,y+1,1])
            board[x][y+1] = 1
        if board[x][y-1] == 0:
            board[x][y-1] = float('inf')
            DFS(distance+1, board, [x,y-1,z])
            board[x][y-1] = 0
        if board[x][y-1] ==1 and z  == 0:
            board[x][y-1] = float('inf')
            DFS(distance+1, board, [x,y-1,1])
            board[x][y-1] = 1
    return

DFS(1, board, [1,1,0])
if answer ==float('inf'):
    print(-1)
else:
    print(answer)