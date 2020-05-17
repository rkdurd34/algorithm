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
    mid_num = num_list[int(len(num_list)/2)]
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
    print(small, big, m)
    return quick(small) +m + quick(big)
    

x = [1,3,2,6,6,3,10,23,123]

print(quick(x))

group = ['A', 'B', 'C', 'D', 'E', 'F']
name = ['가영', '나은', '다희', '라율']

all_list = [group[0],list(name[:2]),group[1],list(name[2:4])]

arr = [10, 3, -62, 1, 82, 55, -48, 63, 47, -63, 93, 92 ]
p = arr[0]
L , M , R = [],[],[]
print(p)
for x in arr:
   if x < p:
       L.append(x)
   elif x > p:
       R.append(x)
   else:
       M.append(x)
print(id(L),id(M),id(R))
a = 1
b = a
a = 2
print(a,b)
c =d= [1,2,3,4]
d.append([5,6,7,8])
print(c,d)
d = [12,3,4]
print(c,d)
class Person:
    name='gdsssss'
    # def __init__(self):
        # self.name = name
def changeName(person):
    person = Person(  )
    

def changeName_1(person):
    person.name = 'galid'

p1 = Person()
changeName(p1)
print(p1.name)
changeName_1(p1)
print(p1.name)

num_list = [1,2,3,4,5,6,7,8,9,10]
num_list[:-1] = 'prime number'
print(num_list)
num_list[4] = [80]
num_list[4:6] = 'kang'
print(num_list)
