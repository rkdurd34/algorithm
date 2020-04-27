import sys


num_input = int(input())
num_list=[int(sys.stdin.readline()) for i in range(num_input)]
print(num_list)
num_list.sort()

a = round(sum(num_list)/len(num_list))
b = num_list[int(len(num_list)/2)]

# def  getTop(list_1):
#     count  =1
#     top = -1
#     for i in range(len(list_1)):
#         c = list_1.count(list_1[i])
#         if c > count :
#             count = c
#             top = list_1[i]
#     return top
# c = getTop(num_list)


# count_name = {}
# result = []
# for i in num_list:
#     count_name[str(i)] = num_list.count(i)
# for key,value in count_name.items():
#     if max(count_name.values()) == value:
#         result.append(key)
# result.sort()
# if len(result) >=2:
#     c = result[1]
# else:
#     c = result[0]

result_dict= {}
for i in num_list:
    result_dict[i] = num_list.count(i)
finished = False
t = 0
while finished == False:
    if max(result_dict.values())==t:
        top = t
        break
    else:
        t+=1
final_result =[]
for key,value in result_dict.items():
    if value == t:
        final_result.append(key)
final_result.sort()
if len(final_result) >=2:
    c = final_result[1]
else:
    c = final_result[0]






if len(num_list)>=2:
    d = num_list[-1] - num_list[0]
else:
    d = 0
print(a)
print(b)
print(c)
print(d)
