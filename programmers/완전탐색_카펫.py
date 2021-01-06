def solution(brown, yellow):
    answer = []
    for i in range(1,(brown-4)//2):
        if ((brown-4)//2 - i)* i == yellow and i+2>=((brown-4)//2 - i)+2:
            answer = [i+2,((brown-4)//2 - i)+2]
            return answer
    return answer