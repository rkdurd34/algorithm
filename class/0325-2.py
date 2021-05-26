import sys
n = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
k = int(sys.stdin.readline())
low, mid, high = 0, (len(num_list)-1)//2, len(num_list)-1 # 이분 탐색을 하기 위해 초기값 세팅

while True:
    temp = num_list[mid]                # 중간값 설정
    if k < temp:                        # 중간값이 목표값보다 큰 경우
        high = mid                      # 중간값을 높은 값으로 설정
        mid = (low + high)//2           # 중간값 다시 세팅
    elif k > temp:                      # 중간값이 목표값보다 작은 경우
        low = mid                       # 작은값을 큰값으로 설정
        mid = (low + high)//2           # 중간값 다시 세팅
    elif k == temp:                     # 같은 경우 루프 종료
        break
    if mid == high or mid == low:       # 이분 탐색 종료 조건
        if abs(num_list[low] - k) > abs(num_list[high]-k):      # 높은 값이 목표값과의 차이가 더 낮은 경우
            temp = num_list[high]
        elif abs(num_list[low] - k) < abs(num_list[high]-k):    # 낮은 값이 목표값과의 차이가 더 낮은 경우
            temp = num_list[low]
        elif abs(num_list[low] - k) == abs(num_list[high]-k):   # 낮은값과 목표값이 같은 경우
            temp = num_list[low]
        break
print(temp)
# 5
# 20 30 40 55 60
# 36
