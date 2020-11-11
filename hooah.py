def solution(n, horizontal):
    
    answer = []
    global count
    count = 0
    
    for i in range(n+2):
        if i==0 or i == n+1:
            answer.append([999]*(n+2))
        else:
            answer.append([999]+[0]*n+[999])
    # print(answer)
    def upperright(index):
        global count
        while index[0]-1 != 0 and index[1]+1 != n+1:
            count += 2 
            index[0] -=1
            index[1] +1
            answer[index[0]][index[1]] = count 
    def downleft(index):
        global count
        while index[1]-1 != 0 and index[0]+1 != n+1:
            # print(answer)
            count += 2
            index[0] +=1
            index[1] -=1
            answer[index[0]][index[1]] = count
    right_check = 0
    down_check = 0
    index = [1,1]
    if horizontal:
        while index != [n,n]:
            print(answer, index)
            if index[0] ==1 or index[1] == n:
                count +=1
                index[1] +=1
                answer[index[0]][index[1]] = count
                downleft(index)
                
            if index[1]==1 or index[1] == n:
                index[0] +=1
                upperright(index)
                
            
    
        
        
    return answer
solution(4, True)