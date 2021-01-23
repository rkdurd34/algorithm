import sys
sys.setrecursionlimit(10**6)
node = int(sys.stdin.readline())
czen = list(map(int, sys.stdin.readline().split()))
graph = dict()
check = []
for i in range(node):
    graph[i] = []
    check.append(False)
for _ in range(node-1):
    a, b = list(map(int, sys.stdin.readline().split()))
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)
dp = [[0, 0] for _ in range(node)]


def dfs(start):
    check[start] = True
    dp[start][0] = czen[start]
    for i in graph[start]:
        if check[i] == False:
            dfs(i)
            dp[start][0] += dp[i][1]
            dp[start][1] += max(dp[i][0], dp[i][1])

    return


dfs(0)
print(max(dp[0][1], dp[0][0]))
