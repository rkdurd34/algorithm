
n = 3
m = 5
if n>m:
    a=n
    b=m
else:
    a=m
    b=n
c=[]
d=[]
e=[]
for i in range(a):
    if a % (i+1) ==0:
        c.append(i+1)

for i in range(b):
    if b % (i+1)==0:
        d.append(i+1)
print(c,d)

for i in d:
    if i in c:
        e.append(i)
print(max(e))
for i in range(a,a*b+1):
    if i % a == 0 and i % b ==0:
        min_num = i
        break
print(min_num)