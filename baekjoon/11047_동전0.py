import sys
num_input = list(map(int,sys.stdin.readline().split()))


coin_num = num_input[0]
coin_amount = num_input[1]
coin_list = []

for i in range(coin_num):
    temp = int(sys.stdin.readline())
    if temp <= coin_amount:
        coin_list.append(temp)

count = 0

for i in range()
while coin_amount >0:
    index = coin_list.pop()
    if coin_amount >= index :
        while coin_amount >= index:
            coin_amount -= index
            count +=1


print(count)

import sys
num_input = list(map(int,sys.stdin.readline().split()))
coin_num = num_input[0]
coin_amount = num_input[1]
coin = []
def min_calc(value,coin):
    a = []
    for i in coin:
        a.append([value-i,i])
    res = a[0]
    for i in a:
        if res[0] > i[0] and i[0] > 0:
            res = i
    return res  

for i in range(coin_num):
    temp = int(sys.stdin.readline())
    coin.append(temp)

value = [coin_amount, 0]
dic = {}
for i in coin: 
    dic[i] = 0
while True:
    value = min_calc(value[0], coin)
    if value[0] < 0:
        break
    else:
        dic[value[1]]+=1
print(dic)