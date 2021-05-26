
import sys
n, m = list(map(int, sys.stdin.readline().split()))
board = [[] for _ in range(n)]


for i in range(m):
    a, b = list(map(int, sys.stdin.readline().split()))
    board[a].append(b)
    board[b].append(a)


def DFS(board, n, m):
    count = 0
    result = []
    visited = [False] * n
    for i in range(len(board)):
        if visited[i] == True:
            continue
        else:
            people = 1
            visited[i] = True
            need_visit = board[i]
            while need_visit:
                temp = need_visit.pop()
                if visited[temp] == False:
                    people += 1
                    visited[temp] = True
                    need_visit.extend(board[temp])

            result.append(people)
            count += 1
    print(count)
    print(max(result), min(result))
    # print(result)
    return


DFS(board, n, m)


# com_num = int(sys.stdin.readline())
# all_dict = dict()
# visited = [False]
# for i in range(com_num):
#     all_dict[i+1] = []
#     visited.append(False)

# line_num = int(sys.stdin.readline())
# for _ in range(line_num):
#     start, end = list(map(int, sys.stdin.readline().split()))
#     all_dict[start].append(end)
#     all_dict[end].append(start)


# def dfs(start_node, graph, visited):
#     need_visit = [start_node]
#     result = -1
#     while need_visit:
#         node = need_visit.pop()
#         if visited[node] == False:
#             result += 1
#             visited[node] = True
#             need_visit.extend(graph[node])
#     return result


# result = dfs(1, all_dict, visited)

# print(result)
