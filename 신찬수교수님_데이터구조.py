# for i in range(10):
#     for j in range(i):
#         print(' ', end='')
#     print('*')
# for i in range(5):
#     for j in range(i):
#         print('*', end ='')
#     print('*')

# for i in range(5):
#     print("*"*(i+1))


# def fib(n):
#     if n ==0:
#         return 0
#     if n ==1:
#         return 1
#     else:
#         return fib(n-2) +fib(n-1)
# print(fib(7))

# result_list = []
# for i in range(1,1001):
#     num_list = []
#     for j in range(1,i+1):
#         if i % j == 0:
#             num_list.append(j)
#     if sum(num_list[:-1]) == i:
#         result_list.append(i)
# print(result_list)

# def sum(a,b):
#     if a ==b : return a
#     if a >b : return 0
#     m = (a+b)//2
#     return sum(a,m) + sum(m+1, b)
# print(sum(1,10))
# def reverse(A):
#     if len(A) == 1: return A
#     return reverse(A[1:]) + A[:1]
# a= []
# print(bool(a))
def quick(num_list):
    print(num_list)
    if len(num_list)==1:
        return num_list
    if len(num_list)==0:
        return []
    
    mid_num = num_list[0]
    small = []
    big = []
    m = []
    for i in num_list:
        if i > mid_num:
            big.append(i)
        if i < mid_num:
            small.append(i)
        if i == mid_num:
            m.append(i)
    print(small, big)
    return quick(small) + [m] + quick(big)
    

x = [1,3,2,6,6,3,10,23,123]

print(quick(x))
