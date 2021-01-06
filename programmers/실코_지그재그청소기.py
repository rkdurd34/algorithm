from collections import deque

def solution(n,horizontal):
    board = []
    for i in range(n+2):
        if i == 0 or i == n+1:
            board.append([1 for i in range(n+2)])
        else:
            board.append([1]+ [0 for i in range(n)]+[1])
    print(board)
    cursor = [1,1]
    count = 0 
    def search(east_index, south_index, eastsouth, up_index, down_index, updown,count ,cursor,board):
        while cursor != [n,n]:
            print(cursor)
            if updown == 1 and eastsouth == 0:
                if south_index == 0:
                    if cursor[0]+1 == n+1:
                        east_index = 0
                        south_index = 1
                    else:
                        cursor = [cursor[0]+1, cursor[1]]
                        east_index = 0
                        south_index = 1
                        eastsouth = 1
                        updown = 0
                        count +=1
                        board[cursor[0]][cursor[1]] = count
                elif east_index == 0:
                    if cursor[1]+1 == n+1:
                        east_index = 1
                        south_index = 0
                    else:
                        cursor = [cursor[0],cursor[1]+1]
                        east_index = 1
                        south_index = 0
                        eastsouth = 1
                        updown = 0
                        count +=1
                        board[cursor[0]][cursor[1]] = count
            elif eastsouth == 1 and updown == 0:
                if down_index == 0:
                    while cursor[1] != 1 and cursor[0] != n:
                        cursor = [cursor[0]+1,cursor[1]-1]
                        count +=2
                        board[cursor[0]][cursor[1]] = count
                        down_index =1
                        up_index = 0
                        updown =1
                        eastsouth = 0
                elif up_index==0:
                    while cursor[1] != n and cursor[0]!=1 :
                        cursor = [cursor[0]-1,cursor[1]+1]
                        count +=2
                        board[cursor[0]][cursor[1]] = count
                        down_index =0
                        up_index = 1
                        updown =1
                        eastsouth = 0
        return board
    if horizontal:
        answer = search(0,1,0,1,0,1,0,[1,1],board)
    else:
        answer = search(1,0,0,0,1,1,0,[1,1],board)

            
    print(answer)     
    return

a = solution(5,False)