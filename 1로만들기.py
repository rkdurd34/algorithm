a = int(input())
num_list = [a]


def func(list_1):
    plus_list = []    
    for i in list_1:
        if i % 2 == 0 :
            plus_list.append(i // 2)
        if i % 3 == 0 :
            plus_list.append(i // 3)
        plus_list.append(i-1)
    return plus_list

i=0
while True:
    if a==1:
        print(i)
        break
    num_list = func(num_list)
    i += 1
    print(min(num_list))
    if min(num_list) ==1:
        print(i)
        break 











# N = int(input())
result_list = [0, 0, 1, 1]

for num in range(4, N + 1):
    process_cnt = 999999999
    if(num % 3 == 0):
        process_cnt = min(process_cnt, result_list[int(num/3)] + 1)
    if(num % 2 == 0):
        process_cnt = min(process_cnt, result_list[int(num/2)] + 1)
    process_cnt = min(process_cnt, result_list[num -1] + 1)
    
    result_list.append(process_cnt)
print(result_list[N])


# a = 135
# print(str(a))
# print(int(str(a)))
# num = 135
# for i in range(1,num+1):
#     x= list(map(int,str(i)))
# print(type(x[0]))

# a = "강경욱"
# b = list(map(str,a))
# print(b)