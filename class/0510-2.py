import sys

m, n = list(map(int, sys.stdin.readline().split()))
board = []

for i in range(m):
    board.append(list(map(int, sys.stdin.readline().split())))
# dp = list(board[-2])
dp = list(board[-1])
# dp = list(board[-2])

for i in range(len(board)-2, -1, -1):  # 첫번째 행은 위에서 했으므로 2번째 행부터 루프
    temp = list(dp)
    for j in range(len(board[i])):
        if j-1 >= 0 and j+1 < len(board[i]):
            dp[j] = board[i][j] + min(temp[j-1], temp[j], temp[j+1])
        elif j-1 < 0:
            dp[j] = board[i][j] + min(temp[j], temp[j+1])
        elif j+1 == len(board[i]):
            dp[j] = board[i][j] + min(temp[j-1], temp[j])
print(dp)

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
