import sys
num = int(sys.stdin.readline())  # 입출력
dp = ([0]*4) + [0] * num  # dp 리스트 초기화
dp[3] = 1   # dp리스트 초기화
for i in range(4, len(dp)):
    dp[i] = dp[i-1] + dp[i-3] + dp[i-4]  # dp 경우의 수 갱신
print(dp[-1])
