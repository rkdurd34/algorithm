import sys
import heapq
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
def dijkstra(graph, begin):
    distances = {node: float('INF') for node in graph.keys()}
    distances[begin] = 0
    queue = []
    heapq.heappush(queue, [distances[begin], begin])
    while queue:
        # print(queue)
        current_distance, current_node = heapq.heappop(queue)
        if distances[current_node] < current_distance:
            continue
        for adjacent, temp_dist in graph[current_node]:
            if current_distance + temp_dist < distances[adjacent]:
                distances[adjacent] = current_distance + temp_dist
                heapq.heappush(queue, [current_distance + temp_dist, adjacent])
