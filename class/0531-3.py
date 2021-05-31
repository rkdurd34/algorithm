
import sys
n, m = list(map(int, sys.stdin.readline().split()))
board = [[] for _ in range(n)]


for i in range(m): # 이중리스트로 인접리스트 구현
    a, b = list(map(int, sys.stdin.readline().split()))
    board[a].append(b)
    board[b].append(a)


def DFS(board, n, m):
    count = 0 # 집단 개수 확인
    result = [] # 스택리스트
    visited = [False] * n # 방문 여부 리스트
    for i in range(len(board)):
        if visited[i] == True: # 방문 했을시 스킵
            continue
        else:
            people = 1 # 집단 내부 명수 확인
            visited[i] = True # 방문 표시
            need_visit = board[i] # 방문 친구와 이어진 관계 스택에 추가
            while need_visit:
                temp = need_visit.pop() # DFS 진행
                if visited[temp] == False: # 방문 안했을시
                    people += 1 # 명수 추가
                    visited[temp] = True # 방문 표시
                    need_visit.extend(board[temp]) # 다음 방문 추가

            result.append(people) # 한 집단 인원수 추가
            count += 1 # 집단 수 추가
    print(count)
    print(max(result), min(result))
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

# import sys
# n, m = map(int, sys.stdin.readline().split())

# adj = [[] for _ in range(n)]

# for _ in range(m):
#     src, dest = map(int, sys.stdin.readline().split())
#     adj[src].append(dest)
#     adj[dest].append(src)

# print(adj)
# # 현재 adj는 이중 리스트 형태로 인접 리스트를 구현한 상태


# def dfs(v, visited):
#     people = 0
#     stack = [v]
#     while stack:
#         v = stack.pop()
#         if v not in visited:
#             visited.append(v)
#             people += 1
#             for w in adj[v]:
#                 stack.append(w)

#     return visited, people


# visited = []
# relationship = 0
# result = []
# for i in range(n):
#     visited, people = dfs(i, visited)
#     if people != 0:
#         relationship += 1
#         result.append(people)
# print(relationship)
# print(max(result),min(result))
