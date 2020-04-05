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
