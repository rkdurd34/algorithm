import sys
vertex = int(sys.stdin.readline())
graph = dict()
result = [1] + ([0] * (vertex-1))
for i in range(vertex-1):
    start, end = list(map(int, sys.stdin.readline().split()))
    try:
        graph[start].append(end)
    except:
        graph[start] = [end]
    try:
        graph[end].append(start)
    except:
        graph[end] = [start]
stack = [1]
while stack:
    temp_list = []
    for j in stack:
        for i in graph[j]:
            if result[i-1] == 0:
                result[i-1] = j
                temp_list.append(i)
    stack = list(temp_list)

for i in range(1, len(result)):
    print(result[i])
