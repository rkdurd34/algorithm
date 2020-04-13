M_31 = [1,3,5,7,8,10,12]
M_30 = [4,6,9,11]
M_29 = [2]
ALL = 0

ALL = 0

a = 6
b = 2
for i in range(a-1):
    print(i+1)
    if i+1 in M_31:
        ALL += 31
    if i+1 in M_30:
        ALL += 30
    if i+1 in M_29:
        ALL += 29
ALL  +=b
print(ALL)
if ALL % 7 == 1:
    print("fri")
if ALL % 7 == 2:
    print('sat')
if ALL % 7 == 3:
    print('sun')
if ALL % 7 == 4:
    print('mon')
if ALL % 7 == 5:
    print('tue')
if ALL % 7 == 6:
    print('wed')
if ALL % 7 == 0:
    print('thu')
