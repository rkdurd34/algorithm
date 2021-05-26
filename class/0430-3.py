import sys
n, k = list(map(int, sys.stdin.readline().split()))

way = list(map(int, sys.stdin.readline().split()))

cost = [0] + list(map(int, sys.stdin.readline().split()))
# 비용 배열에 맞게 dp 초기화
dp = [0] + [float('inf')] * (len(cost)-1)


for i in range(1, len(cost)):
    for j in range(len(way)-1, -1, -1): # 계단 올라갈 수 있는 가짓 수만큼 모두 검사
        if i-way[j] >= 0 and dp[i-way[j]] != float('inf'): 
            # 바닥에서 올라 올 수 있는 조건 검사 후
            # 이미 밟힌 계단인지 검사 후
            for k in range(len(way)): # 최소값 으로 갱신
                dp[i] = min(dp[i], cost[i] + cost[i-way[k]]) 
            # 가장 큰 경우의 수에서 걸릴 경우 작은 수는 검사 할 필요 없으므로 break
            break

# 마지막 계단 밟히지 않은 경우 -1 출력
if dp[-1] == float('inf'):
    print(-1)
else:
    print(dp[-1])
