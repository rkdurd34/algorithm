# import sys

# m, n = list(map(int, sys.stdin.readline().split()))
# board = []

# for i in range(m):
#     board.append(list(map(int, sys.stdin.readline().split())))
# # dp = list(board[-2])
# dp = [0] * n
# # dp = list(board[-2])

# for i in range(len(board)-1, -1, -1):  # 첫번째 행은 위에서 했으므로 2번째 행부터 루프
#     print(dp)
#     for j in range(len(board[i])):
#         if j-1 >= 0 and j+1 < len(board[i]):
#             print(f'확인 {board[i][j]}, {dp[j]}, {dp[j-1]}')
#             dp[j] += min(board[i][j], board[i][j-1], board[i][j+1])
#         elif j-1 < 0:
#             print(f'확인 왼{board[i][j]}, {dp[j]}, {dp[j-1]}')
#             dp[j] +=  min(board[i][j+1], board[i][j])
#         elif j+1 == len(board[i]):
#             print(f'확인 오{board[i][j]}, {dp[j]}, {dp[j-1]}')
#             dp[j] +=  min(board[i][j], board[i][j-1])
# print(dp)


# print(dp[-1])

# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
n=int(input('정수 n의 값을 입력하세요'))
i = 0
def pfunc(a1,a2,i):
    if a1 > n or a2> n:
        return
    print(i)
    print(a1,end=', ')
    print(a2,end=', ')
    a1=a1+a2
    a2=a1+a2
    i+=1
    pfunc(a1,a2,i)
		
print(pfunc(0,1,i),end='')