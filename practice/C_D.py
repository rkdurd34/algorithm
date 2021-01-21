# def solution(v):
#     x_list = []
#     y_list = []
#     answer = []
#     for i in v:
#         x_list.append(i[0])
#         y_list.append(i[1])
#     print(x_list,y_list)
#     for x in x_list:
#         if x_list.count(x) == 1:
#             answer.append(x)
#             break
#     for y in y_list:
#         if y_list.count(y) == 1:
#             answer.append(y)
#             break
#     return answer
# v = [[1, 4], [3, 4], [3, 10]]
# print(solution(v))

# arr = [3,2,4,4,2,5,2,5,5]

# arr = [3,5,7,9,1]
# arr = [1,2,3,3,3,4,4]
# def solution(arr):
#     answer =[]
#     index_list = []

#     for i in arr:
#         if i not in index_list:
#             index_list.append(i)
#     for j in index_list:
#         count_num = arr.count(j)
#         if count_num > 1:
#             answer.append(count_num)
#     if answer==[]:
#         return print(-1)
#     else:
#         return print(answer)
        

    
    
# kang = {'sd':123}
# print(kang.keys())
arr1 = [1,4,1,3,5,6,10]
arr2 = [9,2,3,1,3,4,10]
# arr1 = [1,1,9,4,1,3,11]
# arr2 = [2,3,3,13,12,9,9]
# arr1 = [1,2,2,3,2,2,2]
# arr2 = [4,5,4,5,4,5,4]
# arr1 = [1,5,7,2,9,13,10]
# arr2 = [2,3,9,10,4,8,11]
# arr1 = [1,1,9,4,1,3,11]
# arr2 = [2,3,3,13,12,9,9]
def pair_search(arr1,arr2):
    pair_search_1 = {}
    pair_search_2 = {}

    for i in arr1:
        pair_num = arr1.count(i)
        if pair_num >4:
            pair_num=4

        if pair_num > 1:
            if pair_search_1 =={}:
                pair_search_1[i] = pair_num
            elif pair_search_1[list(pair_search_1.keys())[0]] < pair_num:
                pair_search_1.clear()
                pair_search_1[i] = pair_num
            elif pair_search_1[list(pair_search_1.keys())[0]] == pair_num and list(pair_search_1.keys())[0] < i:
                pair_search_1.clear()
                pair_search_1[i] = pair_num
    if pair_search_1 == {}:
        pair_search_1['none'] = 0

    for i in arr2:
        pair_num = arr2.count(i)
        if pair_num >4:
            pair_num=4

        if pair_num > 1:
            if pair_search_2 =={}:
                pair_search_2[i] = pair_num
            elif pair_search_2[list(pair_search_2.keys())[0]] < pair_num:
                pair_search_2.clear()
                pair_search_2[i] = pair_num
            elif pair_search_2[list(pair_search_2.keys())[0]] == pair_num and list(pair_search_2.keys())[0] < i:
                pair_search_2.clear()
                pair_search_2[i] = pair_num
    if pair_search_2 == {}:
        pair_search_2["none"] = 0
    return [pair_search_1,pair_search_2]
def pair_compare(arr1,arr2):
    if arr1[list(arr1.keys())[0]] > arr2[list(arr2.keys())[0]]:
        print(1)
    if arr1[list(arr1.keys())[0]] < arr2[list(arr2.keys())[0]]:
        print(2)
    if arr1[list(arr1.keys())[0]] == arr2[list(arr2.keys())[0]]:
        if list(arr1.keys())[0] > list(arr2.keys())[0]:
            print(1)
        if list(arr1.keys())[0] < list(arr2.keys())[0]:
            print(2)
        else:
            print(0)
    
    return
a,b = pair_search(arr1,arr2)
print(a,b)
pair_compare(a,b)



# square = {2:4, -3:9, -1:1, -2:4}
# key1 = max(square)
# print(key1)
# key2 = max(square,key = lambda k: square[k])
# print(key2)
# print(square[key2])


# a = [1,2,3]
# b = [100,102,103]
# print(list(zip(a,b)))