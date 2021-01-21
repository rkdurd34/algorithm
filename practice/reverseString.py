# a = "hello"
# b = 'abcdefg'
# def sol(word):
#   word = list(word)
#   for i in range(len(word)//2):
#     word[i], word[-i-1] = word[-i-1], word[i] 

#   return "".join(word)
# c = sol(a)
# print(c)



answer=[[26, 40, 83], [89, 86, 83], [96, 172, 185]]

a = min(answer[-1])
b = min(min(answer[2][0], answer[2][1]), answer[2][2])
print(a,b)
print(type(a),type(b))