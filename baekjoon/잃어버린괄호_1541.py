import sys
import re
temp = sys.stdin.readline().strip()
num = []
dic = []
index = 0
for i in range(len(temp)):
    if temp[i] == "-" or temp[i] == "+":
        dic.append(temp[i])
        num.append(int(temp[index:i]))
        index = i+1
num.append(int(temp[index:]))
# print(num,dic)

# num = list(map(int, re.split('\W+', temp)))

result = num[0]
status = False
for i in range(len(dic)):

    temp = dic[i]
    # if status == False and temp == "-":
    #     status = True
    #     result -= num[i+1]
    # elif status == False and temp == "+":
    #     result += num[i+1]
    # elif status == True and temp == "+" or temp == "-":
    #     result -= num[i+1]
    
    if status == False and temp == "+":
        result += num[i+1]
    else:
        result-= num[i+1]
        status = True

print(result)
