# import sys
# num,distance = list(map(int,sys.stdin.readline().split()))
# check_list = [False]*num
# result_list=[]
# def DFS(num,depth,check_list,result_list):
    
#     if distance == depth:
#         print(" ".join(result_list))
#         return
#     else:
#         for i in range(num):
#             if depth !=0:
#                 if check_list[i] == False and i > int(result_list[-1])-1:
#                     result_list.append(str(i+1))
#                     check_list[i]=True
#                     DFS(num,depth+1,check_list,result_list)
#                     result_list.pop()
#                     check_list[i]=False
#             else:
#                 if check_list[i]==False:
#                     result_list.append(str(i+1))
#                     check_list[i]=True
#                     DFS(num,depth+1,check_list,result_list)
#                     result_list.pop()
#                     check_list[i]=False
    
# DFS(num,0,check_list,result_list) 
import sys
num,distance = list(map(int,sys.stdin.readline().split()))
check_list = [False]*num
result_list=[]
def DFS(num,depth,check_list,result_list,index):
    
    if distance == depth:
        print(" ".join(result_list))
        return
    else:
        for i in range(index,num):
            if check_list[i]==False:
                result_list.append(str(i+1))
                check_list[i]=True
                index = i
                DFS(num,depth+1,check_list,result_list,index)
                result_list.pop()
                check_list[i]=False 
DFS(num,0,check_list,result_list,0) 