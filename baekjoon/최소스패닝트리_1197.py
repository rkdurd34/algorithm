import sys
from collections import defaultdict

parent = dict()
rank = dict()


def find(node):
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]


def union(node_v, node_u):
    root1 = find(node_v)
    root2 = find(node_u)

    if rank[root1] > rank[root2]:
        parent[root2] = root1
    else:  # 부트리의 높이가 같은 경우에도 오른쪽 애를 뽑아서 상위로 올려버림
        parent[root1] = root2
        if rank[root1] == rank[root2]:
            rank[root2] += 1


def make_set(node):
    parent[node] = node
    rank[node] = 0


def kruskal(graph, verticles):
    mst = list()
    for node in verticles:
        make_set(node)

    edges = graph
    edges.sort()
    count = 0
    # print(edges)
    for edge in edges:
        weight, node_v, node_u = edge
        if find(node_v) != find(node_u):
            union(node_v, node_u)
            mst.append(edge)
            count += edge[0]
        # print(rank)
        # print(parent)
        # print()
    print(count)
    return mst


# print(sorted(mygraph['edges']))
# print()

v, e = list(map(int, sys.stdin.readline().split()))
board = defaultdict(list)
edges = []
verticles = []
for _ in range(e):
    a, b, c = list(map(int, sys.stdin.readline().split()))
    edges.append([c, a, b])
for i in range(v):
    verticles.append(i+1)
kruskal(graph=edges, verticles=verticles)
