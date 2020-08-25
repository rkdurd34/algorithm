import sys
all_list = []
for i in range(9):
    all_list.append(list(map(int,sys.stdin.readline().split())))
print(all_list)

def is_avilable(row,column):
    column_check = [False]*9
    row_check = [False] *9
    for i in range(9):
        if all_list[row][i]:
            column_check[i+1] = True
        if all_list[i][0]:
            row_check[i+1] = True


    return
def DFS(num,depth,all_list):
    for row in range(len(all_list)):
        for  column in range(len(all_list)):
            if all_list[i][j] == 0:
                if is_available(row,column)