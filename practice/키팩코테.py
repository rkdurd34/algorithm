# import sys
# from itertools import permutations


# A = [1, 2, 3, 4]
# B = [4, 3, 4, 5]
# check_list = list(permutations(A, len(A)))


# def sol(A, B):
#     result = 0
#     for i in range(len(A)):
#         result += A[i]*B[i]
#     return result


# result = float('inf')
# for i in check_list:
#     check = sol(list(i), B)
#     if check < result:
#         result = check
# print(result)


import sys

a = [6, 9, 5, 7, 4]
check = [0 for _ in range(len(a))]
for i in range(len(a)-1, -1, -1):
    temp = a[i]
    for j in range(a.index(a[i])-1, -1, -1):
        if a[i] < a[j]:
            check[i] = j+1
            break
print(check)
