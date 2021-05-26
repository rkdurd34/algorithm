
import sys
n = int(sys.stdin.readline())
board = [[0, 0]]+[list(map(int, sys.stdin.readline().split())) 
                  for _ in range(n)]

time = [0] * (n+1) #DP를 위한 리스트 세팅

for i in range(1, len(board)):
    
    temp = board[i-1][1] + time[i-1] - board[i][0]   # 전 사람의 심사신 + 전에 기다렸던 시간 - 앞사람과의 간격
    if temp > 0:                                     # 시간이 +인 경우에만 time 리스트 업로드
        time[i] = temp

print(format(sum(time)/n, ".1f"))

# 5
# 0 4
# 2 7
# 1 6
# 2 5
# 1 3

# 10
# 0 3
# 3 2
# 3 2
# 3 2
# 3 2
# 3 3
# 3 3
# 3 3
# 3 3
# 3 3

# 3
# 0 3
# 2 4
# 3 3

# 3
# 1 5
# 3 1
# 1 2

2 + 1
