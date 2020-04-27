import sys
num_input = int(sys.stdin.readline())
age_list = []
for i in range(num_input):
    age_list.append(list(sys.stdin.readline().split()))
age_list_sort = sorted(age_list, key=lambda x :int(x[0]))
for [i,j] in age_list_sort:
    print(i,j)