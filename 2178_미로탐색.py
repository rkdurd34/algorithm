import sys
row,col = list(map(int,sys.stdin.readline().split()))
all_list = []
for i in range(row+2):
    if i == 0 or i == row+1:
        all_list.append([0] * (col+2))
    else:
        all_list.append([0]+list(map(int,sys.stdin.readline().strip()))+[0])

start = [1,1]

def BFS(start_node,graph):
    count = 1
    visited, need_visit = list(), list()
    need_visit.append(start_node)
    visited.append(start_node)
    while [row,col] not in visited :
        temp_need_list = list(need_visit)
        temp_list = []
        count +=1
        while temp_need_list:
            try:
                i = need_visit.pop(0)
                if all_list[i[0]+1][i[1]] == 1:
                    if [i[0]+1,i[1]] not in visited:
                        temp_list.append([i[0]+1,i[1]])
                        visited.append([i[0]+1,i[1]])
                if all_list[i[0]][i[1]+1] == 1:
                    if [i[0],i[1]+1] not in visited:
                        temp_list.append([i[0],i[1]+1])
                        visited.append([i[0],i[1]+1])
                if all_list[i[0]-1][i[1]] == 1:
                    if [i[0]-1,i[1]] not in visited:
                        temp_list.append([i[0]-1,i[1]])
                        visited.append([i[0]-1,i[1]])
                if all_list[i[0]][i[1]-1] == 1:
                    if [i[0],i[1]-1] not in visited:
                        temp_list.append([i[0],i[1]-1])
                        visited.append([i[0],i[1]-1])
            except IndexError:
                break
        
        
        need_visit.extend(temp_list)
    print(count)
    return visited
result = BFS(start,all_list)

