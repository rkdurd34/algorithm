# import sys
# import re
# temp = sys.stdin.readline().strip()
# num = []
# dic = []
# index = 0
# for i in range(len(temp)):
#     if temp[i] == "-" or temp[i] == "+":
#         dic.append(temp[i])
#         num.append(int(temp[index:i]))
#         index = i+1
# num.append(int(temp[index:]))
# # print(num,dic)

# # num = list(map(int, re.split('\W+', temp)))

# result = num[0]
# status = False
# for i in range(len(dic)):

#     temp = dic[i]
#     # if status == False and temp == "-":
#     #     status = True
#     #     result -= num[i+1]
#     # elif status == False and temp == "+":
#     #     result += num[i+1]
#     # elif status == True and temp == "+" or temp == "-":
#     #     result -= num[i+1]
    
#     if status == False and temp == "+":
#         result += num[i+1]
#     else:
#         result-= num[i+1]
#         status = True

# print(result)

a = """
===========영화 목록===========
Dark Knight
Harry Porter
Parasite
Matrix
La La Land
==============================
예매하실 영화를 선택해주세요: La La Land를 선택하셨습니다
관람 인원 수를 선택해주세요: 관람할 인원 수는 3명입니다
할인권을 사용하시려면 y, 금액 확인으로 넘어가시려면 n을 입력해주세요: 할인권을 사용하지 않았습니다

<예매 상세 내역>
==============================
영화 제목: La La Land
관람 인원: 3명
합산 금액: 36000원
할인 금액: 0원
------------------------------
실 결제액: 36000원
==============================
"""

b = """
===========영화 목록===========
Dark Knight
Harry Porter
Parasite
Matrix
La La Land
==============================
예매하실 영화를 선택해주세요: La La Land를 선택하셨습니다
관람 인원 수를 입력해주세요: 관람할 인원 수는 3명입니다
할인권을 사용하시려면 y, 금액 확인으로 넘어가시려면 n을 입력해주세요: 할인권을 사용하지 않았습니다

<예매 상세 내역>
==============================
영화 제목: La La Land
관람 인원: 3명
합산 금액: 36000원
할인 금액: 0원
------------------------------
실 결제액: 36000원
==============================
"""
for i in range(len(a)):
    if a[i]!=b[i]:
        print(a[i],b[i],i)