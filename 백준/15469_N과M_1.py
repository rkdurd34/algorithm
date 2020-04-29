
# num_list = list(map(int,input().split()))

num_list = [4,4]
a= num_list[0]
b = num_list[1]
result_list =[]
for i in range(b):
    result_list.append(1)
for i in result_list:
    
for j in range(1,a+1):
    result_list[0] = j
    for i in range(1,a+1):
        result_list[1] = i
        if result_list[0]!=result_list[1]:
            print(result_list)
        
print(result_list)
    
