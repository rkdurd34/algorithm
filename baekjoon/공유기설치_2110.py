# 이분 탐색 검색 기준 -> 거리(답),비교 대상 좌표(상수)
# 항상 답으로 나오는 기준으로 탐색 시도해보기
# -> 최대 거리 -> 거리를 기준으로 고정된 값(집좌표)을 탐색
import sys
from itertools import combinations
input = sys.stdin.readline
n, c = list(map(int, input().split()))

board = sorted([int(input())for i in range(n)])
low = 1
high = board[-1] - board[0]


def binary_search(low, high):
    result = 1
    while low <= high:
        count = 1
        mid = (low+high) // 2
        current = board[0]
        for i in range(1, len(board)):
            if board[i] >= current + mid:
                count += 1
                current = board[i]
        if count >= c:
            result = mid
            low = mid + 1
        else:
            high = mid - 1

    return result


a = binary_search(low, high)
print(a)

# import sys
# from itertools import combinations
# input = sys.stdin.readline
# n, c = list(map(int, input().split()))
# result = 0
# board = [int(input())for i in range(n)]
# check = list(combinations(board, c))
# for i in check:
#     temp_check = list(combinations(i, 2))
#     low = min(temp_check, key=lambda x: abs(x[1]-x[0]))
#     low = abs(low[1]-low[0])
#     if low > result:
#         result = low
#     # print(temp_check)
# # print(board)
# print(result)
