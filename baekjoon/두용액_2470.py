import sys
input = sys.stdin.readline
n = int(input())
board = list(map(int, input().split()))
board.sort()
start = 0
end = len(board)-1
result = float('inf')
answer = []
# print(board)
while start < end:
    # print(start, end, result)
    temp = board[start] + board[end]

    if result > abs(temp):
        result = abs(temp)
        answer = [board[start], board[end]]
        if temp == 0:
            break
    if temp > 0:
        end -= 1
    elif temp < 0:
        start += 1
# print(result)
# print(board[start], board[end])
print(*answer)
