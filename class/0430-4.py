# import sys

# money = int(input())
# day = int(input())
# check_list = []
# for i in range(day):
#     check_list.append(int(input()))

# def winorloss(lst, value):
#     check = value
#     for i in lst:


# import heapq

# nums = [4, 1, 7, 3, 8, 5]
# heap = []

# for num in nums:
#     heapq.heappush(heap, (-num, num))  # (우선 순위, 값)

# while heap:
#     a = heapq.heappop(heap)
#     print(a)  # index 1

import heapq
import sys


def sol(check, n):
    result = 0
    gate = []
    for i in check:
        if len(gate) < n:
            # 게이트 안에 사람이 없을시 도착시간과 기다리는 시간을 더해서 
            # 힙 푸시
            heapq.heappush(gate, i[0]+i[1])
        else:
            # 게이트가 꽉 찬 경우 가장 기다릴 시간이 적은
            # 게이트에서 힙팝 실행
            temp = heapq.heappop(gate)
            # 도착한 시간 보다 검사시간이 길경우
            # 기다려야 하므로 결과값에 추가
            if temp > i[0]:
                result += temp - i[0]
            # 기다린 시간 + 이전시간 사람 추가해서 새로운 시간 갱신
            heapq.heappush(gate, temp+i[1])
    return result


n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
time = 0
check = []

for i in range(k):
    a, b = list(map(int, sys.stdin.readline().split()))
    time += a
    # 총량으로 시간을 계산하기 위해 도착 한 시간 계산
    check.append([time, b])
print(round(sol(check, n)/k, 1))
