import sys
import heapq

node = int(sys.stdin.readline())
graph = dict()
distance = [[float('inf')] * node] * node
# distance = dict()
distance[node] = float('inf')
for i in range(node-1):
    # check.append(False)
    # distance[i+1] = float('inf')
    start, end, dis = list(map(int, sys.stdin.readline().split()))
    try:
        graph[start][end] = dis
    except:
        graph[start] = dict()
        graph[start][end] = dis
    try:
        graph[end][start] = dis
    except:
        graph[end] = dict()
        graph[end][start] = dis


def dij(start, graph, end, distance):
    distance[]
    queue = []
    heapq.heappush(queue, [distance])
    return


# for i in range(edge):
#     dij()


print(graph)
print(check)
print(distance)
