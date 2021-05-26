import sys
import random
n = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
k = int(sys.stdin.readline())


def quick_sort(data_list):                  # 퀵정렬
    if len(data_list) <= 1:                 # 재귀 종료 조건
        return data_list
    left, right, mid = list(),  list(), list()
    pivot = data_list[random.randrange(0, len(data_list)-1)]    # 랜덤으로 리스트 인덱스 설정
    for index in range(0, len(data_list)):                      # 랜덤 인덱스에 따라 low,mid,high 그룹으로 나누기
        if pivot > data_list[index]:                            # 설정값 보다 작은 경우 left에 추가
            left.append(data_list[index])
        elif pivot < data_list[index]:                          # 설정값 보다 큰 경우 right에 추가
            right.append(data_list[index])
        elif pivot == data_list[index]:                         # 설정값과 같은 경우 mid에 추가
            mid.append(data_list[index])
    return quick_sort(left) + mid + quick_sort(right)


num_list = quick_sort(num_list)


def binary_search(k, num_list, low, high):      # 이진 탐색
    mid = (low+high)//2                         # 중간값 설정
    while True:
        temp = num_list[mid]                    # 중간값 설정
        if k < temp:                            # 설정 값보다 큰 경우 중간값을 큰 값으로 설정
            high = mid
            mid = (low + high)//2
        elif k > temp:                          # 설정값 보다 작은 경우 중간값을 작은 값으로 설정 
            low = mid                           
            mid = (low + high)//2
        elif k == temp:
            break
        if mid == high or mid == low:                               # 이분 탐색 종료 조건
            if abs(num_list[low] - k) > abs(num_list[high]-k):      # 설정 값과의 차이가 큰값이 적은 경우 큰값으로 설정
                temp = num_list[high]
            elif abs(num_list[low] - k) < abs(num_list[high]-k):    # 설정 값과의 차이가 작은 값이 적은 경우 작은값으로 설정
                temp = num_list[low]
            elif abs(num_list[low] - k) == abs(num_list[high]-k):   # 작은 값과 큰 값이 같은 경우 작은 값을 설정
                temp = num_list[low]
            break
    return temp, mid


mid_num, mid_index = binary_search(k//2, num_list, 0, len(num_list)-1) # 포문 루프 범위를 위한 목표 값의 반값 구하기

result = [0, float('inf')]
for i in range(0, mid_index+1):             
    temp = k-num_list[i]        #첫번째 인덱스 부터 목표 값을 뺀 후 뺸 값에 대해 가장 가까운 값을 구하기 위해 이분 탐색
    temp_mid_num, temp_mid_index = binary_search(       
        temp, num_list, mid_index, len(num_list)-1) # 목표값과 가장 가장 가깝고 목표값보다 크지 않는 조건
    if abs(sum(result) - k) >= abs(temp_mid_num + num_list[i] - k) and temp_mid_num + num_list[i] <= k:
        if abs(sum(result) - k) == abs(temp_mid_num + num_list[i] - k) and temp_mid_num < result[1]:
            result = [num_list[i], temp_mid_num]
        elif abs(sum(result) - k) > abs(temp_mid_num + num_list[i] - k):
            result = [num_list[i], temp_mid_num]
print(*result)
