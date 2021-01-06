# 항상 BFS에서는 visited를 따로 두고 생각하기!
# BFS 뻗어 나가는 경우수에 따라 3차원 배열 조작해서 분화!
import sys, collections

def BFS():
  dx = [-1,1,0,0]
  dy = [0,0,-1,1]
  visited[0][0][1],visited[0][0][0] = 1,1
  need_visit = collections.deque([[0,0,0]])
  while need_visit:
    x,y,z = need_visit.popleft()
    if [x,y] == [row-1,col-1]:
      return visited[x][y][z]
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if -1 < nx < row and -1 < ny < col:
        if board[nx][ny] == 0 and  visited[nx][ny][z] == 0:
          visited[nx][ny][z] = visited[x][y][z] + 1
          need_visit.append([nx,ny,z])
        if board[nx][ny] == 1 and z == 0:
          visited[nx][ny][1] = visited[x][y][z]+1
          need_visit.append([nx,ny,1])
  return -1

row, col = map(int, sys.stdin.readline().split())
board  = [list(map(int,(list(sys.stdin.readline().strip())))) for _ in range(row)]
visited = [[[0,0] for _ in range(col)] for _ in range(row)]
print(BFS())

# import sys
# row, col = list(map(int, sys.stdin.readline().split()))
# board = []
# for i in range(row+2):
#   if i == 0 or i == row + 1:
#     board.append([float('inf') for _ in range(col+2)])
#   else:
#     board.append([float('inf')] + list(map(int,(list(sys.stdin.readline().strip()))))+ [float('inf')])
# answer = 2
# # 210000
# # 010110
# # 010111
# # 010110
# # 010110
# # 000110
# board = [[float('inf') for _ in range(8)],[float('inf'),0,1,0,0,0,0,float('inf')],[float('inf'),0,1,0,1,1,0,float('inf')],[float('inf'),0,1,0,1,1,1,float('inf')],[float('inf'),0,1,0,1,1,0,float('inf')],[float('inf'),0,1,0,1,1,0,float('inf')],[float('inf'),0,0,0,1,1,0,float('inf')],[float('inf') for _ in range(8)]]
# need_visit  = [[1,1,0]]
# board[1][1]=2
# def BFS(board, need_visit,answer):
  
#   dx = [-1,1,0,0]
#   dy = [0,0,-1,1]
#   test = 0
#   while need_visit:
#     # if test == 7:
#     #   break
#     print(need_visit)
#     print(board)
#     temp_list = []
#     answer+=1
#     for i in need_visit:
#       x,y,z = i

#       if i[:2] == [6,6]:
#           return answer
#       for j in range(4):
#         nx = x + dx[j]
#         ny = y + dy[j]
#         if board[nx][ny] != answer-2 and board[nx][ny]!=1 and board[nx][ny] != float('inf') and board[nx][ny]!=0:
#           temp_list.append([nx,ny,z])
#           board[nx][ny] = answer
#         if board[nx][ny] == 0 :
#           temp_list.append([nx,ny,z])
#           board[nx][ny] = answer
#         if board[nx][ny] == 1 and z == 0:
#           temp_list.append([nx,ny,1])
#     need_visit = list(temp_list)
#     test+=1
    
  
#   return -1
# a = BFS(board,need_visit,answer)
# print(a)

# import sys
# sys.setrecursionlimit(999999999)
# row, col = list(map(int, sys.stdin.readline().split()))
# board = []
# for i in range(row+2):
#   if i == 0 or i == row + 1:
#     board.append([float('inf') for _ in range(col+2)])
#   else:
#     board.append([float('inf')] + list(map(int,(list(sys.stdin.readline().strip()))))+ [float('inf')])
# answer = float('inf')
# board[1][1] = True

# def DFS(distance, board, index):
#     # print(index)
#     global answer
#     if index[:2] == [row,col]:
#         if answer > distance:
#             answer = distance
#         return
    
#     else:
#         x = index[0]
#         y = index[1]
#         z = index[2]
#         if board[x+1][y] == 0:
#             board[x+1][y] = float('inf')
#             DFS(distance+1, board, [x+1,y,z])
#             board[x+1][y] = 0
#         if board[x+1][y] ==1 and z  == 0:
#             board[x+1][y] = float('inf')
#             DFS(distance+1, board, [x+1,y,1])
#             board[x+1][y] = 1
#         if board[x-1][y] == 0:
#             board[x-1][y] = float('inf')
#             DFS(distance+1, board, [x-1,y,z])
#             board[x-1][y] = 0
#         if board[x-1][y] ==1 and z  == 0:
#             board[x-1][y] = float('inf')
#             DFS(distance+1, board, [x-1,y,1])
#             board[x-1][y] = 1
#         if board[x][y+1] == 0:
#             board[x][y+1] = float('inf')
#             DFS(distance+1, board, [x,y+1,z])
#             board[x][y+1] = 0
#         if board[x][y+1] ==1 and z  == 0:
#             board[x][y+1] = float('inf')
#             DFS(distance+1, board, [x,y+1,1])
#             board[x][y+1] = 1
#         if board[x][y-1] == 0:
#             board[x][y-1] = float('inf')
#             DFS(distance+1, board, [x,y-1,z])
#             board[x][y-1] = 0
#         if board[x][y-1] ==1 and z  == 0:
#             board[x][y-1] = float('inf')
#             DFS(distance+1, board, [x,y-1,1])
#             board[x][y-1] = 1
#     return

# DFS(1, board, [1,1,0])
# if answer ==float('inf'):
#     print(-1)
# else:
#     print(answer)