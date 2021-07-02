import sys
input = sys.stdin.readline
n = int(input())
board = list(map(int, input().split()))
m = int(input())
check = list(map(int, input().split()))

result = 0
board.sort()
highest = board[-1]
for i in check:
    if i > highest:
        print(0)
        continue
    found = False
    low = 0
    high = len(board)-1
    while low <= high:
        mid = (low + high) // 2
        if board[mid] == i:
            found = True
            break
        elif board[mid] < i:
            low = mid + 1
        elif board[mid] > i:
            high = mid - 1
    if found == True:
        print(1)
    elif found == False:
        print(0)


# import sys
# input = sys.stdin.readline
# n = int(input())
# board = list(map(int, input().split()))
# m = int(input())
# check = list(map(int, input().split()))


# board.sort()
# result = [0] * board[-1]
# # print(result)
# for i in range(len(board)):
#     temp = board[i]-1
#     result[temp] = 1

# for j in check:
#     if j-1 < len(board):
#         print(result[j-1])
#     else:
#         print(0)
