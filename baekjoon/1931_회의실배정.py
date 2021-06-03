# import sys
# num_input = int(sys.stdin.readline())
# start_list = []
# finish_list = []

# for i in range(num_input):
#     start,finish = list(map(int,sys.stdin.readline().split()))
#     start_list.append(start)
#     finish_list.append(finish)


# search_finished = True
# count = 0
# order = 0
# while search_finished:

#     if order ==0:
#         temp_pivot = min(finish_list)
#         pivot_index = finish_list.index(temp_pivot)
#         del start_list[pivot_index], finish_list[pivot_index]
#         count +=1
#         order+=1
#     else:
#         print(temp_pivot)
#         if temp_pivot > max(start_list):
#             print(count)
#             search_finished = False
#         else:
#             compare_list = []
#             for i in range(len(start_list)):
#                 if start_list[i] >=temp_pivot:
#                     compare_list.append([finish_list[i],i])
#             temp_pivot = sorted(compare_list, key = lambda x : x[0])[0][0]
#             pivot_index = finish_list.index(temp_pivot)
#             del start_list[pivot_index], finish_list[pivot_index]
#             count+=1


import sys
n = int(sys.stdin.readline())
board = []
big = 0
for i in range(n):
    temp = list(map(int, sys.stdin.readline().split()))
    a, b = temp
    if big < a:
        big = a
    if big < b:
        big = b
    board.append(temp)
check = [False for _ in range(big+1)]

board.sort(key=lambda x: (x[1], x[0]))
result = 0
end_time = 0
for i in board:
    start,end = i
    if start >= end_time:
        end_time = end
        result +=1

print(result)
