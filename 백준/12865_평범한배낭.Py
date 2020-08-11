import sys 
num,amount = map(int, sys.stdin.readline().split())
item_list= [[0,0]]
check_list = [[0]*(amount+1)]
for _ in range(num):
    item_list.append(list(map(int,sys.stdin.readline().split())))
    check_list.append([0]*amount+[0])




for i in range(1,len(check_list)):
    for j in range(1,len(check_list[i])):
        if j >= item_list[i][0]:
            check_list[i][j] =max(check_list[i-1][j],item_list[i][1]+check_list[i-1][j-item_list[i][0]])
        else:
            check_list[i][j] = check_list[i-1][j]
print(check_list[num][amount])
# for i in range(1,len(check_list)):
#     for j in range(len(check_list[i])):        
        
#         if j+1>= item_list[i][0]:
        
#             if len(check_list[i])>= item_list[i][0]+j+1:
#                 print(f'i:{i} j:{j}')
#                 temp = item_list[i][0] + j+1
#                 check_list[i][temp-1] = max(item_list[i][1]+check_list[i-1][temp-1],check_list[i-1][temp-1])
#             else:
#                     check_list[i][j] =max(check_list[i-1][j],item_list[i][1])
#         else:
#             check_list[i][j] = check_list[i-1][j]
#         print(check_list)

        