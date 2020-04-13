
arr = [1,1,3,3,0,1,1]
i=0
while i <= len(arr)-2:
    if  arr[i]==arr[i+1]:
        del arr[i+1]
    else:
        i+=1    
    
# 효율성 테스트 실패...
    


        