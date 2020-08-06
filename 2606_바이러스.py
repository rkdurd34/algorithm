import sys
com_num = int(sys.stdin.readline())
all_dict = dict()
for i in range(com_num):
    all_dict[i+1] = []
    
line_num = int(sys.stdin.readline())
for _ in range(line_num):
    start,end = list(map(int,sys.stdin.readline().split()))
    all_dict[start].append(end)
    all_dict[end].append(start)
def dfs(start_node, graph):
    visited , need_visit = list(),list()
    need_visit.append(start_node)
    while need_visit:
        node = need_visit.pop(0)
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])
    return visited
result = dfs(1,all_dict)[1:]

print(len(result))

