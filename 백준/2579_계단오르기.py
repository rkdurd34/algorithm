import sys
num = int(sys.stdin.readline())
result_list = [0,0]

for i in range(num):
    result_list.append(int(sys.stdin.readline()))
check_list = list(result_list)
for i in range(2,len(result_list)):
    if i == 2:
        continue
    else:
        result_list[i] = max((check_list[i-2]+result_list[i-3]+check_list[i]),(result_list[i-3]+check_list[i-1]+check_list[i]))
print(result_list)