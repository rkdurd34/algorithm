import sys
input = sys.stdin.readline
k, n = list(map(int, input().split()))
board = [int(input()) for i in range(k)]
low = 1
high = 2**31 - 1
result = 1
while low <= high:
    mid = (low+high)//2
    count = 0
    for i in board:
        temp = i // mid
        count += temp
    if count >= n:
        # print(mid,'sya')
        low = mid + 1
        if result < mid:
            result = mid
        # else:
        #     break
    elif count > n:
        low = mid + 1
    elif count < n:
        high = mid - 1
print(result)
