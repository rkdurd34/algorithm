import sys


def sol(n):
    if n == 1:
        return 1
    check = [True] * (2*n)
    m = int(n ** 0.5)
    for i in range(2, m):
        if i % 
        if check[i-1] == True:
            for j in range(i+1, n, i):
                check[j] = False

    return check.count(True) - 2


while 1:
    a = int(input())
    if a == 0:
        break
    else:
        print(prime_list(a))

# # check = []
# a = 1
# while a != 0:
#     a = int(sys.stdin.readline())
#     if a == 0:
#         break
#     if a == 1:
#         print(1)
#         continue
#     count = 0
#     for i in range(a+1, 2*a):
#         for j in range(2, i):
#             if i % j == 0:
#                 break
#             elif j == i-1 and i % j != 0:
#                 # print(i)
#                 count += 1
#     print(count)
#     # check.append(a)
# # check.sort(reverse=True)
# # for i in range(len(check)-2, -1, -1):
