from itertools import permutations

def solution(numbers):
    answer = 0
    check_set = set()
    # print(set(map("".join,permutations(numbers,len(numbers)))))
    for i in range(len(numbers)):
        for k in set(map("".join,permutations(numbers,i+1))):
            if int(k) !=1 and int(k) !=0:
                check_num = 0
                for j in range(2,int(k)):
                    if int(k)%j ==0:
                        check_num +=1
                        break
                if check_num == 0:
                    check_set.add(int(k))
                # print(int(k), i,k, check_set)
                
            
    
    return len(check_set)