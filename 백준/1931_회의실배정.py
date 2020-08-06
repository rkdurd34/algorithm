import sys
# num_input = int(sys.stdin.readline())
all_list = [[1, 4], [3, 5], [0, 6], [5, 7], [3, 8], [5, 9], [6, 10], [8, 11], [8, 12], [2, 13], [12, 14]]
# for i in range(num_input):
#     count  = 0 
#     temp_list = []
#     temp = list(map(int,sys.stdin.readline().split()))
#     all_list.append(temp)
# print(all_list)

count = 0 
start_time = 5
for i in range(len(all_list)):
    if all_list[i][0] < start_time:
        all_list[i][0] = start_time
