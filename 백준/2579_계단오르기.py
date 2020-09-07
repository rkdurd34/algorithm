import sys
num = int(sys.stdin.readline())
result_list = [0]+([0]*num)
check_list = [0]
for i in range(num):
    check_list.append(int(sys.stdin.readline()))

for i in range(1,len(result_list)):
    if i == 1:
        result_list[i] = check_list[i]
        continue
    if i ==2:
        result_list[i] = check_list[i]+check_list[i-1]
    else:
        result_list[i] = max(result_list[i-2]+check_list[i], result_list[i-3]+check_list[i-1]+check_list[i])

print(result_list[-1])
