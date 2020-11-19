def solution (n, times):
    answer = 0
    times.sort()
    high = n * times[0]
    low = 0
    mid = n * times[0]//2
    final = float('inf')
    found = False
    while  low <= high and high > 0 and low >= 0:
        # print(low,mid,high,final)
        for i in range(len(times)):
            answer += mid // times[i]
        if answer < n:
            high = high
            low = mid+1
            mid = (high+low)//2
            answer = 0 
        elif answer > n:
            if final > mid:
                final = mid
            high = mid-1
            low = low
            mid = (high+low)//2
            answer = 0
        elif answer == n:
            if final > mid:
                final = mid
            high = mid-1
            low = low
            mid = (high+low)//2
            answer = 0
    return final
# def solution (n, times):
#     answer = 0
#     times.sort()
#     high = n * times[0]
#     low = 0
#     mid = (high + low) // 2
    
#     temp = 0
#     for i in range(high):
#         for j in range(len(times)):
#             answer += i // times[j]
#         if answer == n :
#             return i
#         else:
#             answer = 0