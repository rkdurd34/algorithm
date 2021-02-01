import sys
def dfs(depth, start, end, result):
    if start == end:
        return depth
    temp = graph[start]
    for i in temp:
        if check[i-1] == False:
            check[i-1] = True
            result = dfs(depth+1, i, end, result)
            check[i-1] = False
    return result

people_num = int(sys.stdin.readline())
start, end = list(map(int, sys.stdin.readline().split()))
edge = int(sys.stdin.readline())

graph = dict()

for i in range(people_num):
    graph[i+1] = []

for i in range(edge):
    par, chi = list(map(int, sys.stdin.readline().split()))
    graph[par].append(chi)
    graph[chi].append(par)
check = [False for _ in range(people_num)]
print(dfs(0, start, end, -1))
# if result:
#     print(result)
# else:
#     print(-1)
