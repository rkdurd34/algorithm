def insertion_sort(data_list):
    for  stand in range(len(data_list)):
        key =  data_list[stand]
        for num in range(stand,0,-1):
            if key < data_list[num-1]:
                data_list[num-1],  data_list[num]=data_list[num], data_list[num-1]
            else:
                break
    return data_list
data_list = [9,3,2,5]
print(insertion_sort(data_list))
