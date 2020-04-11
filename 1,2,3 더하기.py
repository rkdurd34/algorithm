a = int(input())
c = []
for i in range(a):
    c.append(int(input()))
print(c)
num_list = [1,2,3]
for i in c:
    base_list=[]

    for j in    range(i):
        base_list.append(0)
    print(base_list)
    # for index,value in  enumerate(base_list):
    #     while sum(base_list) <=i:
    #         base_list[index] = 1
    #         print(base_list)



print((100/1.1)+(1100/1.21))
print(int(1100//1.1))

a = "\t Python \t"
b = ">>> I like Python <<<"


print(a.strip("\t ")+"\n"+b.strip("><"))