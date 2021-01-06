def solution(N,number):
    check = []
    for i in range(8):
        check.append({int(str(N)*(i+1))})
    # print(check)
    for i in range(len(check)):
        for j in range(i):
            for a in check[j]:
                for b in check[i-j-1]:
                    check[i].add(a+b)
                    if a-b >0:
                        check[i].add(a-b)
                    check[i].add(a*b)
                    if b != 0:
                        check[i].add(a//b)
        
        if number in check[i]:
            return i+1
        
    return -1
# def solution(N,number):
#     check = list()
#     check.append({N})
#     for i in range(8):
#         check.append({int(str(N)*(i+1))})
#     # print(check)
#     for i in range(1,len(check)-1):
#         for j in check[i-1]:
#             if j == number:
#                 return i 
#             if int(str(N)*(i))-j>0:
#                 check[i].add(int(str(N)*(i))-j)
#             if j!= 0:
#                 check[i].add(int(str(N)*(i))//j)
#             if int(str(N)*(i))*j <= 32000 and int(str(N)*(i))+j<=32000:
#                 check[i].add(int(str(N)*(i))+j)
#                 check[i].add(int(str(N)*(i))*j)
#         # print(check)
    
#     return -1


# def solution(N, number):
#     answer = []
#     def BFS(check_list, N,depth):
#         # print(check_list, depth)
#         if depth ==9:
#             return 
#         temp_list = []
#         for  i in check_list:
#             temp_list.extend([i+N, i//N, i*N,  i-N ])
#             if i == N or i == 11*N or i== 111*N or i == N*1111 or i == N*11111 or i == N*1111111 or i == N *111111 or i==N*11111111:
#                 temp_list.extend([int(str(i)+str(N))])
#                 if int(str(i)+str(N)) == number:
#                     answer.append(depth+1)
#                     return
#             if i + N == number or i//N ==number or i*N == number  or i-N == number :
#                 answer.append(depth+1)
#                 return
#         BFS(temp_list, N, depth+1)            
#     BFS([N], N, 1)
    
#     if answer:
#         return answer[0]
#     else:
#         return -1

# def solution(N, number):
#     answer = 0
#     N_ = N
#     check_list = [N_+N, N_//N, N_*N, int(str(N_)+str(N)), N_-N ]
#     def BFS(check_list, N,depth):
#         temp_list = []
#         for  i in check_list:
#             temp_list.extend([i+N, i//N, i*N, int(str(i)+str(N)), i-N ])
#             if i + N == number or i//N ==number or i*N == number or int(str(i)+str(N)) == number or i-N == number :
#                 return depth
#             else:
#                 BFS(temp_list, N, depth+1)            
#     BFS(check_list, N, len(str(number))-1)
#     return answer