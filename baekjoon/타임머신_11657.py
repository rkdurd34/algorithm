import sys
N, M = list(map(int, sys.stdin.readline().split()))
graph = {}
for i in range(N):
    graph[i+1] = []
for i in range(M):
    start, end, dist = list(map(int, sys.stdin.readline().split()))
    try:
        graph[start].append([end, dist])
    except:
        graph[start] = [[end, dist]]
print(graph)
