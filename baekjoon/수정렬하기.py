num_input = int(input())
num_list=[]
for i in range(num_input):
    num_list.append(int(input()))
num_list.sort()
for i in num_list:
    print(i)