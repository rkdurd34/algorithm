import heapq


def dijkstra(graph, start):

    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        if distances[current_node] < current_distance:
            continue
        for adjacent, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(queue, [distance, adjacent])
    return distances


graph = {
    'a': {'b': 8, 'c': 1, 'd': 2},
    'b': {},
    'c': {'b': 5, 'd': 2},
    'd': {'e': 3, "f": 5},
    'e': {'f': 1},
    'f': {'a': 5}
}

print(dijkstra(graph, 'a'))
