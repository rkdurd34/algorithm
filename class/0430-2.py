import sys
num = int(sys.stdin.readline())
cost = [0]+list(map(int, sys.stdin.readline().split()))
# 3가지 경우의 수중 한가지에서 최소 값
for i in range(1, len(cost)):
    if i-4 >= 0:    # 4계단 밑에서 올라 올 수 있는 경우의 수
        cost[i] += min(cost[i-1], cost[i-3], cost[i-4])
    elif i-3 >= 0: # 3계단 밑에서 올라올 수 있는 경우의 수
        cost[i] += min(cost[i-1], cost[i-3])
    elif i-1 >= 0: # 1계단 밑에서 올라 올 수 있는 경우의 수
        cost[i] += cost[i-1]
print(cost[-1])

