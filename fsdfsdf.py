def solution(n, board):
    answer = []
    revised_board = list()
    check_board = list()
    for i in range(n+2):
        if i==0 or i == n+1:
            revised_board.append([999]*(n+2))
            check_board.append([999]*(n+2))
        else:
            revised_board.append([999]+board[i-1]+[999])
            check_board.append([999]+[False]*len(board[i-1])+[999])
    def SEARCH(target,stack, revised_board,check_board):
        temp= list(check_board)
        if target == n**2+1:
            return len(answer)
        while stack:
            temp_list = []
            for i in range(len(stack)):
                x = stack[i][0]
                y = stack[i][1]
                if revised_board[x][y] == target:
                    answer.append(1)
                    check_board = list(temp)
                    return SEARCH(target+1, [[x,y]], revised_board,check_board)
                if x-1 == 0:            # 위끝에서 아래끝으로 이동 / 위로 이동
                    temp_list.append([n,y])
                    check_board[n][y] = True
                    
                elif x-1 != 0 :
                    temp_list.append([x-1,y])
                    check_board[x-1][y] = True
                    
                if y-1 == 0 :             # 왼쪽끝에서 오른쪽으로 이동 / 왼쪽 이동
                    temp_list.append([x,n])
                    check_board[x][n] = True
                elif y-1 != 0 :
                    temp_list.append([x,y-1])
                    check_board[x][y-1] = True
                if x+1 == n+1 :             # 아래끝에서 위끝으로 이동 / 아래로이동
                    temp_list.append([1,y])
                    check_board[1][y] = True
                elif x+1 != n+1 :
                    temp_list.append([x+1,y])
                    check_board[x+1][y] = True
                if y+1 == n+1 :             # 오른쪽끝에서 왼쪽으로 이동 / 오른쪽으로 이동
                    temp_list.append([x,1])
                    check_board[x][1] = True
                elif y+1 != n+1 :
                    temp_list.append([x, y+1])
                    check_board[x][y+1] = True
            
            stack = list(temp_list)
            answer.append(1)
        
        
    
    
    SEARCH(1,[[1,1]],revised_board,check_board)
        
    
            
    return len(answer)
print(solution(3,[[3, 5, 6], [9, 2, 7], [4, 1, 8]]))
# def solution(n, board):
#     answer = []
#     revised_board = list()
#     check_board = list()
#     for i in range(n+2):
#         if i==0 or i == n+1:
#             revised_board.append([999]*(n+2))
#             check_board.append([999]*(n+2))
#         else:
#             revised_board.append([999]+board[i-1]+[999])
#             check_board.append([999]+[False]*len(board[i-1])+[999])
#     temp= list(check_board)
    
#     def BFS(target,stack, revised_board):
#         print('몆번',stack)
#         check_board = list(temp)
#         print(check_board)
#         if target+1 == (n**2)+1:
#             return len(answer)
#         while stack:
#             temp_list = []
#             for i in range(len(stack)):
                
#                 x = stack[i][0]
#                 y = stack[i][1]
#                 if revised_board[x][y] == target:
#                     return BFS(target+1, [[x,y]], revised_board)
#                 if x-1 == 0 and check_board[n][y] == False:            # 위끝에서 아래끝으로 이동 / 위로 이동
#                     temp_list.append([n,y])
#                     check_board[n][y] = True
                    
#                 elif x-1 != 0 and check_board[x-1][y] == False:
#                     temp_list.append([x-1,y])
#                     check_board[x-1][y] = True
                    
#                 if y-1 == 0 and check_board[x][n] == False:             # 왼쪽끝에서 오른쪽으로 이동 / 왼쪽 이동
#                     temp_list.append([x,n])
#                     check_board[x][n] = True
#                 elif y-1 != 0 and check_board[x][y-1] == False:
#                     temp_list.append([x,y-1])
#                     check_board[x][y-1] = True
#                 if x+1 == n+1 and check_board[1][y]== False:             # 아래끝에서 위끝으로 이동 / 아래로이동
#                     temp_list.append([1,y])
#                     check_board[1][y] = True
#                 elif x+1 != n+1 and check_board[x+1][y]== False:
#                     temp_list.append([x+1,y])
#                     check_board[x+1][y] = True
#                 if y+1 == n+1 and check_board[x][1]==False:             # 오른쪽끝에서 왼쪽으로 이동 / 오른쪽으로 이동
#                     temp_list.append([x,1])
#                     check_board[x][1] = True
#                 elif y+1 != n+1 and check_board[x][y+1]==False:
#                     temp_list.append([x, y+1])
#                     check_board[x][y+1] = True
#             print(temp_list)
#             stack = list(temp_list)
#             answer.append(1)
        
        
    
    
#     BFS(1,[[1,1]],revised_board)
        
    
            
#     return len(answer)
# print(solution(3,[[3, 5, 6], [9, 2, 7], [4, 1, 8]]))