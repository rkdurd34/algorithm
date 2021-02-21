import sys
import heapq
N, E = list(map(int, sys.stdin.readline().split()))
graph = {}
result = []
for i in range(N+1):
    graph[i+1] = []
    result.append(0)

for i in range(E):
    start, end, dist = list(map(int, sys.stdin.readline().split()))
    try:
        graph[start].append([end, dist])
    except:
        graph[start] = [[end, dist]]
    try:
        graph[end].append([start, dist])
    except:
        graph[end] = [[start, dist]]
mid = list(map(int, sys.stdin.readline().split()))


def dijkstra(graph, start):
    distances = {node + 1: float('inf') for node in range(len(graph))}
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        if current_distance > distances[current_node]:
            continue
        for adjacent, weight in graph[current_node]:
            distance = weight + current_distance
            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(queue, [distance, adjacent])

    # print(distances)
    return distances


distances = dijkstra(graph, 1)
# print(result, mid, distances)
for i in mid:
    result[i] += distances[i]

#     print(distances[i], distances[4])
# print(graph, result)
for i in range(len(mid)):

    distances = dijkstra(graph, mid[i])
    result[mid[i]] += distances[mid[i-1]]
    result[mid[i-1]] += distances[N]
a = min(result[mid[0]], result[mid[1]])
if a == float('inf'):
    print(-1)
else:
    print(a)
