col, row = list(map(int, input().split()))
board = []
for i in range(col+2):
    if i == 0 or i == col+1:
        board.append([float('inf')] * (row+2))
    else:
        board.append([float('inf')] + list(input()) + [float('inf')])
# print(board)
visited = [board[1][1]]
need_visit = [1,1]
global final
final = 1
def DFS(depth, board,need_visit):
    global final
    if final < depth:
        final = depth
    x = need_visit[0]
    y = need_visit[1]
    if board[x+1][y] not in visited and board[x+1][y] != float('inf'):
        visited.append(board[x+1][y])
        DFS(depth+1, board, [x+1,y])
        visited.pop()
    if board[x][y+1] not in visited and board[x][y+1] != float('inf'):
        visited.append(board[x][y+1])
        DFS(depth+1, board, [x,y+1])
        visited.pop()
    if board[x][y-1] not in visited and board[x][y-1] != float('inf'):
        visited.append(board[x][y-1])
        DFS(depth+1, board, [x,y-1])
        visited.pop()
    if board[x-1][y] not in visited and board[x-1][y] != float('inf'):
        visited.append(board[x-1][y])
        DFS(depth+1, board, [x-1,y])
        visited.pop()
DFS(1,board, need_visit)  
print(final)
        
