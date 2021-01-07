import sys
num_input = int(sys.stdin.readline())
check = [list(map(int, sys.stdin.readline().split())) for i in range(num_input)]

for i in range(1,len(check)):
  for j in range(len(check[i])):
    check[i][j] += min(check[i-1][:j]+check[i-1][j+1:])
print(min(check[-1]))


def answer(L):
    DP = [[0, 0, 0] for _ in range(len(L[0]))]
    DP[0] = [L[0][0], L[1][0], 0]
    for i in range(1, len(L[0])):
        DP[i][0] = max(DP[i - 1][1], DP[i - 1][2]) + L[0][i]    # 현재 위를 선택할 때
        DP[i][1] = max(DP[i - 1][0], DP[i - 1][2]) + L[1][i]    # 현재 아래를 선택할 때
        DP[i][2] = max(DP[i - 1])   # 아무것도 선택 안할 때

    return max(DP[-1])

import sys
input = sys.stdin.readline

t = int(input())
T = []
for i in range(t):
    x = []
    