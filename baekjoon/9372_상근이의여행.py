import sys
test_case = int(sys.stdin.readline())
for i in range(test_case):
    country, air = list(map(int, sys.stdin.readline().split()))
    for j in range(air):
        num = list(map(int, sys.stdin.readline().split()))
    print(country - 1)


# import sys
# from collections import defaultdict

# parent = dict()
# rank = dict()

# def find(node):
#     if parent[node] != node:
#         parent[node] = find(parent[node])
#     return parent[node]


# def union(node_v, node_u):
#     root1 = find(node_v)
#     root2 = find(node_u)

#     if rank[root1] > rank[root2]:
#         parent[root2] = root1
#     else:
#         parent[root1] = root2
#         if rank[root1] == rank[root2]:
#             rank[root2] += 1


# def make_set(node):
#     parent[node] = node
#     rank[node] = 0


# def kruskal(graph):
#     mst = list()
#     for node in graph['verticles']:
#         make_set(node)

#     edges = graph['edges']
#     edges.sort()
#     print(edges)
#     for edge in edges:
#         weight, node_v, node_u = edge
#         if find(node_v) != find(node_u):
#             union(node_v, node_u)
#             mst.append(edge)
#         print(rank)
#         print(parent)
#         print()
#     return mst


# test_case = int(sys.stdin.readline())

# for i in range(test_case):
#   board = defaultdict(list)
#   n,m = list(map(int,sys.stdin.readline().split()))
#   for j in range(m):
#     a,b = list(map(int,sys.stdin.readline().split()))
#     board[a].append(b)
#     board[b].append(a)
#     kruskal(graph=board)

#   # print(country - 1)
