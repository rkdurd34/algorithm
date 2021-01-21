# import sys
# node = int(sys.stdin.readline())
# czen = list(map(int, sys.stdin.readline().split()))
# graph = dict()
# check = []
# for i in range(node):
#     graph[i] = []
#     check.append(False)
# for _ in range(node-1):
#     a, b = list(map(int, sys.stdin.readline().split()))
#     graph[a-1].append(b-1)
#     graph[b-1].append(a-1)
# dp = [[0,0] for _ in range(node)]
# def dfs(start):
#   check[strat] = True
#   dp[start][0] =

