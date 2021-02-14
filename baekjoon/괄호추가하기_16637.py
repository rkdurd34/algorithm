import sys
length = int(sys.stdin.readline())
board = "+" + sys.stdin.readline().strip()
board += "+0"
check = [{(0, int(board[1]))}]
for _ in range(length//2 + 1):
    check.append(set())

dx = ["+", "-", "*"]

for i in range(len(check)-1):
    temp_index = 2 * i + 1+1
    for j in check[i]:
        if j[1] == -1:
            check[i+1].add((j[0], int(board[temp_index+1])))
        elif j[1] != -1:
            if dx.index(board[temp_index-2]) == 0:
                check[i+1].add((j[0]+j[1], int(board[temp_index+1])))
                if dx.index(board[temp_index]) == 0:
                    check[i+1].add((j[0]+(j[1]+int(board[temp_index+1])), -1))
                if dx.index(board[temp_index]) == 1:
                    check[i+1].add((j[0]+(j[1]-int(board[temp_index+1])), -1))
                if dx.index(board[temp_index]) == 2:
                    check[i+1].add((j[0]+(j[1]*int(board[temp_index+1])), -1))
            if dx.index(board[temp_index-2]) == 1:
                check[i+1].add((j[0]-j[1], int(board[temp_index+1])))
                if dx.index(board[temp_index]) == 0:
                    check[i+1].add((j[0]-(j[1]+int(board[temp_index+1])), -1))
                if dx.index(board[temp_index]) == 1:
                    check[i+1].add((j[0]-(j[1]-int(board[temp_index+1])), -1))
                if dx.index(board[temp_index]) == 2:
                    check[i+1].add((j[0]-(j[1]*int(board[temp_index+1])), -1))
            if dx.index(board[temp_index-2]) == 2:
                check[i+1].add((j[0]*j[1], int(board[temp_index+1])))
                if dx.index(board[temp_index]) == 0:
                    check[i+1].add((j[0]*(j[1]+int(board[temp_index+1])), -1))
                if dx.index(board[temp_index]) == 1:
                    check[i+1].add((j[0]*(j[1]-int(board[temp_index+1])), -1))
                if dx.index(board[temp_index]) == 2:
                    check[i+1].add((j[0]*(j[1]*int(board[temp_index+1])), -1))
# print(check)
# print(max(check[-1]))
# print(max(check[-1])[0])
# a = sorted(check[-1], key=lambda x: (x[0], x[1]))
b = max(check[-1], key=lambda x: (x[0], x[1]))
print(b[0])
# print(a[-1][0])
# print(a)
# print(a[-1][0])
# print(a[-1][0])
# result = 0
# for i in check[-1]:
#     if dx.index(board[-2]) == 0:
#         if i[1] == -1:

#         elif i[1] != -1:
#     if dx.index(board[-2]) == 1:
#     if dx.index(board[-2]) == 2:
#     if i[1] == -1:
#     elif i[1] != -1:

# if dx.index(board[temp_index]) == 0:
#     check[i+1].add((j[0]+j[1], int(board[temp_index+1])))
#     if dx.index(board[temp_index-2]) == 0:
#         check[i+1].add((j[0]+(int(board[temp_index+1])+int(board[temp_index-1])),-1))
#     if dx.index(board[temp_index-2]) == 1:
#         check[i+1].add((j[0]-(int(board[temp_index+1])+int(board[temp_index-1])),-1))
#     if dx.index(board[temp_index-2]) == 1:
#         check[i+1].add((j[0]*(int(board[temp_index+1])+int(board[temp_index-1])),-1))
# if dx.index(board[temp_index]) == 1:
#     check[i+1].add((j[0]-j[1], int(board[temp_index+1])))
#     if dx.index(board[temp_index-2]) == 0:
#         check[i+1].add((j[0]+(int(board[temp_index+1])+int(board[temp_index-1])),-1))
#     if dx.index(board[temp_index-2]) == 1:
#         check[i+1].add((j[0]-(int(board[temp_index+1])+int(board[temp_index-1])),-1))
#     if dx.index(board[temp_index-2]) == 1:
#         check[i+1].add((j[0]*(int(board[temp_index+1])+int(board[temp_index-1])),-1))
# if dx.index(board[temp_index]) == 0:
#     check[i+1].add((j[0]+j[1], int(board[temp_index+1])))
#     if dx.index(board[temp_index-2]) == 0:
#         check[i+1].add((j[0]+(int(board[temp_index+1])+int(board[temp_index-1])),-1))
#     if dx.index(board[temp_index-2]) == 1:
#         check[i+1].add((j[0]-(int(board[temp_index+1])+int(board[temp_index-1])),-1))
#     if dx.index(board[temp_index-2]) == 1:
#         check[i+1].add((j[0]*(int(board[temp_index+1])+int(board[temp_index-1])),-1))
# while check:
#     temp_list = []
#     for i in check:
#         if i[1] == -1:
#         elif i[1] != -1:

# if i[1] == -1:
# elif i[1] != -1:
#     if board[index].index(dx) == 0:
#         temp_list.append([i[0]+i[1], board[index+1], 0])
#         temp_list.append([i[0]+i[1]+board[index+1],-1,0])
#     if board[index].index(dx) == 1:
#         temp_list.append([i[0]-i[1], board[index+1], 1])
#         temp_list.append([i[0]+i[1]-board[index+1],-1,1])
#     if board[index].index(dx) == 2:
#         temp_list.append([i[0]*i[1], board[index+1], 1])
#         temp_list.append([i[0]+i[1]*board[index+1],-1,2])
# index += 1


# # a = ["+", "+", "-"]
# # b = "3+8*7-9*2"
# # for i in range(1, len(b), 2):
# #     print(b[i])


# print(3+8*7-9*2)
