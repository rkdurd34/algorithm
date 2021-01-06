def solution(answers):
    answer = [0,0,0]
    hoo = []
    a = [1,2,3,4,5] * 2000
    b = [2,1,2,3,2,4,2,5] * 1250
    c = [3,3,1,1,2,2,4,4,5,5] * 1000
    check_a=0
    check_b=0
    check_c=0
    max = 0
    for i in range(len(answers)):
        if a[i] == answers[i]:
            answer[0]+=1
        if b[i] == answers[i]:
            answer[1]+=1
        if c[i] == answers[i]:
            answer[2]+=1
    for i in range(len(answer)):
        if answer[i]>max:
            max = answer[i]
            hoo = list()
            hoo.append(i+1)
        elif answer[i] == max:
            hoo.append(i+1)
            
    hoo.sort()
    return hoo