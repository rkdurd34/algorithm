data_list =[1,9,3,2]
for num in range(len(data_list)):
    swap = 0
    for index in range(len(data_list)-num-1):
        # print(data_list, f'index = {index}', f'num = {num}',f'len(data_list)-num -1 = {len(data_list)-num-1}')
        if data_list[index] > data_list[index+1]:
            data_list[index],data_list[index+1] = data_list[index+1],data_list[index]
            swap +=1
            # print(swap)
    if swap==0:
        break
# print(data_list, swap)
        
def bubble_sort(data_list):
    for index in range(len(data_list)):
        swap = 0
        for index2 in range(len(data_list)-1 -index):
            if data_list[index2]> data_list[index2 +1]:
                data_list[index2],data_list[index2+1] = data_list[index2+1],data_list[index2]
                swap += 1
        if swap ==0:
            break
    return data_list
print(bubble_sort(data_list))
