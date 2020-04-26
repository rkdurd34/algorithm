x = int(input())
c =list()
for i in range(x,0-1,-1):
    a = str(i)
    z = i
    for j in range(len(a)):
        z += int(a[j])
    if z == x :
        c.append(i)

if c:
    print(c[-1])
else:
    print(0)




















x = int(input())
c =list()
for i in range(x):
    a = str(i)
    z = i
    for j in range(len(a)):
        z += int(a[j])
    if z == x :
        c.append(i)
if c:
    print(c[0])
else:
    print(0)














# num = 216

# answer = 0

# for i in range(1,num):
#     x = list(map(int,str(i)))
#     y = i + sum(x)
#     if y ==num :
#         answer = i 
#         break
# print(i)

num = 216
answer = 0
for i in range(1,num):
    x = map(int,str(i))
    # print("sum(x)값 : ", sum(x), f'i값 : {i}')    
    
    y = sum(x) +i
    # print("y값이후","sum(x)값 : ", sum(x), f'i값 : {i}',f'y값 : {y}')    
    if y == num:
        answer = i 
        break
print(answer)

# print(answer)
# print("sum(x)값 : ", sum(x), f'i값 : {i}',x)
# print("y = sum(x) + i 코드 이후의 sum(x)값 : ", sum(x), f'i값 : {i}',x)
#     print("sum(x)+i == num 값:", sum(x)+i == num,"sum(x)타입:",type(sum(x)), "num타입",type(num), "y타입",type(y))
#     print('y값 :',y ,"sum(x)+i값",i + sum(x))
#     print()

