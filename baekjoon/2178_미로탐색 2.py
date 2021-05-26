import sys
row, col = list(map(int, sys.stdin.readline().split()))
board = []
for i in range(row):
    board.append(list(map(int, sys.stdin.readline().strip())))

start = [0, 0]

def BFS(start, board, row, col):
    count = 1
    board[0][0] = 0
    
    need_visit = [start]
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    while need_visit:
        temp_list = []
        for i in need_visit:
            x = i[0]
            y = i[1]
            for j in range(len(dx)):
                new_x = x+dx[j]
                new_y = y + dy[j]
                if 0 <= new_x < row and 0 <= new_y < col:
                    if board[new_x][new_y] == 1:
                        temp_list.append([new_x, new_y])
                        board[new_x][new_y] = 0
            if i == [row-1, col-1]:
                print(count)
                return
        need_visit = temp_list
        count += 1


BFS(start, board, row, col)


# import sys
# num, column = list(map(int,sys.stdin.readline().split()))
# all_list = []
# for i in range(num+2):
#     if i ==0 or i == num+1:
#         all_list.append([0]*(column+2))
#     else:
#         all_list.append([0] + list(map(int,sys.stdin.readline().strip())) + [0])
# loc = [1,1]
# count = 1


# # 여기서부터=는 시간 초과 코드
# result = []
# # print(all_list)
# def DFS(loc):

#     # print(loc,all_list)
#     # print(loc)
#     global count
#     if loc[0] == num and loc [1] == column:
#         result.append(count)
#         return
#     if all_list[loc[0]][loc[1]+1] == 1:
#         # print('우')
#         all_list[loc[0]][loc[1]+1] = 0
#         loc[1]  +=1
#         count +=1
#         DFS(loc)
#         all_list[loc[0]][loc[1]] = 1
#         loc[1] -= 1
#         count -=1
#     if all_list[loc[0]+1][loc[1]] == 1:
#         # print('하')
#         all_list[loc[0]+1][loc[1]] = 0
#         loc[0]  += 1
#         count +=1
#         DFS(loc)
#         all_list[loc[0]][loc[1]] = 1
#         loc[0] -=  1
#         count -=1
#     elif all_list[loc[0]][loc[1]-1] == 1:
#         # print('좌')
#         all_list[loc[0]][loc[1]-1] = 0
#         loc[1]  -= 1
#         count +=1
#         DFS(loc)
#         all_list[loc[0]][loc[1]] = 1
#         loc[1] +=  1
#         count -=1
#     elif all_list[loc[0]-1][loc[1]] == 1:
#         # print('상')
#         all_list[loc[0]-1][loc[1]] = 0
#         loc[0]  -= 1
#         count +=1
#         DFS(loc)
#         all_list[loc[0]][loc[1]] = 1
#         loc[0] +=  1
#         count -=1
#     else:
#         return
# DFS(loc)
# print(min(result))
