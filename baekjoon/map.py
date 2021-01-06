# def split(n):
#     result = int(n)
#     return result
# num_input = int(input())
# a=[]
# for i in range(num_input):
#     a.append(list(map(split,input().split())))
#     a = input().split()
#     print(a)
li=[1,2,3]
result = list(map(lambda i:i**2, li))

list_1 = ['23','21', '13','12','11',]
result = list(sorted(list_1, key=lambda x: (x[0], x[1])))
print(result)