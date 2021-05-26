import sys
m, n = list(map(int, sys.stdin.readline().split()))
board = []
for i in range(m):
    temp = list(map(int, sys.stdin.readline().split()))
    board.append(temp)

dp = list(board[-1])  # 1차원 dp 배열 초기화

for i in range(1, len(dp)):  # 첫번째 행은 오른쪽으로 밖에 가지 못하므로 왼쪽값 추가
    dp[i] += dp[i-1]

for i in range(m-2, -1, -1):  # 첫번째 행은 위에서 했으므로 2번째 행부터 루프
    for j in range(len(board[i])):  # 밑에서 올라왔을 경우 값 변경
        dp[j] += board[i][j]

    for k in range(1, len(board[i])):  # 밑에서 올라오는경우와 왼쪽에서 오는 경우의 수
        dp[k] = min(dp[k], dp[k-1] + board[i][k])  # 비교 후 작은 값으로 업데이트

print(dp[-1])

# # print(board)
# for i in range(len(board)-1, -1, -1):
#     for j in range(len(board[i])):
#         if j-1 >= 0 and i+1 < len(board):
#             board[i][j] += min(board[i+1][j], board[i][j-1])
#         elif j-1 >= 0 and i+1 >= len(board):
#             board[i][j] += board[i][j-1]
#         elif j-1 < 0 and i+1 < len(board):
#             board[i][j] += board[i+1][j]


# print(board[0][-1])
4 5
2 8 9 5 8
4 4 6 5 3
5 7 5 1 1
3 2 5 4 8