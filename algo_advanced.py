graph = dict()

graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'G', 'H', 'I']
graph['D'] = ['B', 'E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']
print(graph)

def dfs(graph,start_node):
    visited, need_visit = list(),list()
    need_visit.append(start_node)

    while need_visit:
        print(need_visit)
        node = need_visit.pop()
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])
    return visited
dfs(graph,'A')

def bfs(graph, start_node):
    visited = list()
    need_visit = list()
    need_visit.append(start_node)
    while need_visit:
        print(need_visit)
        node = need_visit.pop(0)
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])
    return visited
bfs(graph,"A")

coin_list = [500,100,50,1]
def min_coin_count(value,coin_list):
    total_coin_count=0
    details = list()
    coin_list.sort(reverse=True)
    for coin in coin_list:
        coin_num = value //coin
        total_coin_count += coin_num
        value -= coin_num * coin
        details.append([coin,coin_num])
    return total_coin_count, details
print(min_coin_count(4720,coin_list))
string = "12345"
comma = ','

print(comma.join(string))
hoo =  []
for i in range(1,5):
    hoo.append(i)
print(hoo)
