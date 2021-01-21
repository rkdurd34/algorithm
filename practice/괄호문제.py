
num_input = input()
alpha = input()
stack = []

def sol(alpha):
    count = 0
    for i in alpha:
        if i == "[":
            count +=1
        elif i == "]" and count > 0:
            count -=1
        elif i ==']' and count ==0:
            answer = False
            return answer
    if count:
        return False
    else:
        return True
print(sol(alpha))