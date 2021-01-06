
# # fp, integer, save, junction = 56*(10**6), 110*(10**6), 80*(10**6), 16*(10**6)

# # cpi1, cpi2, cpi3, cpi4 = 1, 1, 4, 2
# # cpi1_1, cpi2_1, cpi3_1, cpi4_1 = 1*0.6, 1*0.6, 4*0.7, 2*0.7

# # cycletime = 2*(10**9)

# # time = (fp*cpi1/cycletime) + (integer*cpi2/cycletime) + (save*cpi3/cycletime) + (junction*cpi4/cycletime)
# # time_1 = (fp*cpi1_1/cycletime) + (integer*cpi2_1/cycletime) + (save*cpi3_1/cycletime) + (junction*cpi4_1/cycletime)


# # print(time,time_1)
# # print(time/time_1)


# # b=259000000000
# # c=86000000000.0

# # print(b/c)
# def find(list1,dict1, nowIndex, endpoint, answer):
#     temp = 0
#     if nowIndex == endpoint:
#         return answer
#     elif len(list1) < endpoint-nowIndex:
#         return 0
#     for i in range(len(list1)):
#         temp+=find(list1[i+1:],dict1,nowIndex+1,endpoint,answer*dict1[list1[i]])
#     return temp

# from collections import defaultdict
# def solution(clothes):
#     set1,cnt,dict1 = set(),0, defaultdict(int)
#     answer = 0
#     for x,y in clothes:
#         dict1[y]+=1
#         set1.add(y)
#         list1= list(set1)
#     for i in range(len(list1)):
#         answer += find(list1,dict1,0,i+1,1)
#     return answer

print(hex(1<<32))
print(bin((1<<32)-1))
a = "11111111111111111111111111111111".count("1")
print(a)
    