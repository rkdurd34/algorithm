mygraph = {
    'verticles': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
    'edges': [
        (7, 'A', 'B'),
        (5, 'A', 'D'),
        (7, 'B', 'A'),
        (8, 'B', 'C'),
        (9, 'B', 'D'),
        (7, 'B', 'E'),
        (8, 'C', 'B'),
        (5, 'C', 'E'),
        (5, 'D', 'A'),
        (9, 'D', 'B'),
        (7, 'D', 'E'),
        (6, 'D', 'F'),
        (7, 'E', 'B'),
        (5, 'E', 'C'),
        (7, 'E', 'D'),
        (8, 'E', 'F'),
        (9, 'E', 'G'),
        (6, 'F', 'D'),
        (8, 'F', 'E'),
        (11, 'F', 'G'),
        (9, 'G', 'E'),
        (11, 'G', 'F')
    ]
}
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
    else: # 부트리의 높이가 같은 경우에도 오른쪽 애를 뽑아서 상위로 올려버림
        parent[root1] = root2
        if rank[root1] == rank[root2]:
            rank[root2] += 1

# 높이가 다른 부트리들끼리 합칠 때 상황
#
def make_set(node):
    parent[node] = node
    rank[node] = 0


def kruskal(graph):
    mst = list()
    for node in graph['verticles']:
        make_set(node)

    edges = graph['edges']
    edges.sort()

    for edge in edges:
        weight, node_v, node_u = edge
        if find(node_v) != find(node_u):
            union(node_v, node_u)
            mst.append(edge)
        print(rank)
        print(parent)
        print()
    return mst


print(sorted(mygraph['edges']))
print()
kruskal(graph=mygraph)
