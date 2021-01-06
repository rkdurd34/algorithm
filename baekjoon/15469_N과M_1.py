
def f (n,m,k):
    if n==k:
        print(*res)
        return
    else:
        for i in range(m):
            if visited[i]==0:
                visited[i]=1
                res[n] = arr[i]
                print(visited)
                f(n+1,m,k)
                visited[i]=0

a,b = map(int,input().split())

arr = range(1,a+1)
res =[0]*b
visited = [0 for i in range(a)]
# print(arr, res ,visited)
# print(arr[0],arr[1],arr[3])
f(0,a,b)



# def dfs(graph,start_node):
#     visited, need_visit = list(),list()
#     need_visit.append(start_node)

#     while need_visit:
#         print(need_visit)
#         node = need_visit.pop()
#         if node not in visited:
#             visited.append(node)
#             need_visit.extend(graph[node])
#     return visited
# dfs(graph,'A')
    

# num_list = [1,9,3,2]
# for i in range(len(num_list)):
#     swap = 0
#     for j in range(len(num_list)-i-1):
#         if num_list[j] >num_list[j+1]:
#             num_list[j],num_list[j+1] = num_list[j+1],num_list[j]
#             swap+=1
    
# print(num_list)

# N,M = map(int,input().split())
N,M = 4,4
visited = [False] * N
out = []
# print(visited)
def  solve(depth, N,M):
    if depth ==M:
        print(' '.join(map(str,out)))
        
        return
    for i in range(len(visited)):
        if  visited[i] == False:
            visited[i] = True
            out.append(i+1)
            # print(visited, out, i)
            solve(depth+1,N,M)
            # print(visited, out, i , "재귀 이후")
            visited[i] = False
            out.pop()
        

solve(0,N,M)

def sum(n):
    if n ==1:
        return 1
    
    return sum(n-1)+n

print(sum(10))
