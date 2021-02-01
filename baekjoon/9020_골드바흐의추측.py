import sys
from itertools import combinations_with_replacement
case = int(sys.stdin.readline())


# def dfs(check, board, result, depth, temp, index):
#     if depth == 2:
#         result.append(list(temp))
#         return result
#     else:
#         for i in range(index, len(board)):
#             if check[i] == False:
#                 check[i] = True
#                 temp.append(board[i])
#                 dfs(check, board, result, depth+1, temp, i)
#                 temp.pop()
#                 check[i] = False

#     return result


for i in range(case):
    num = int(sys.stdin.readline())
    check = [True] * num
    temp = int(num ** 0.5)
    for i in range(2, temp+1):
        if check[i] == True:
            for j in range(i+i, num, i):
                check[j] = False
    board = []
    for i in range(2, len(check)):
        if check[i] == True:
            board.append(i)

    # check = [False for _ in range(len(board))]
    # comb = dfs(check, board, [], 0, [], 0)
    # comb = combinations_with_replacement(board, 2)

    def sol(board, num):

        result = 0
        diff = float('inf')
        for i in range(len(board)):

            for j in range(i, len(board)):
                a = board[i]
                b = board[j]
                if a+b == num:
                    if abs(a-b) < diff:
                        result = [a, b]
                        diff = abs(a-b)

        return result
    result = sol(board, num)
    print(*result)

    # result = 0
    # diff = float('inf')
    # for i in comb:
    #     if sum(i) == num:
    #         if abs(i[0]-i[1]) < diff:
    #             result = i
    #             diff = abs(i[0]-i[1])
    # print(*result)
