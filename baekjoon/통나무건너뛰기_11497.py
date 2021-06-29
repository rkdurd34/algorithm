import sys
input = sys.stdin.readline
t = int(input())

for _ in range(t):
    result = 0
    n = int(input())
    board = list(map(int, input().split()))
    board.sort()
    board.append(board[-1])
    for i in range(len(board)-1, -1, -1):
        if i-2 >= 0:
            temp = board[i]-board[i-2]
            if temp > result:
                result = temp
    print(result)
