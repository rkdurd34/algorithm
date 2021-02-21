import sys
from itertools import permutations
import copy
N, M, K = list(map(int, sys.stdin.readline().split()))
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
cal = []
temp_cal = [list(map(int, sys.stdin.readline().split())) for _ in range(K)]
check_list = list(permutations(temp_cal, len(temp_cal)))
result = float('inf')
# print(check_list)


def sol(r, c, s, temp_board):
    for i in range(s, 0, -1):
        temp = temp_board[r-i][c+i]
        temp_board[r-i][c-i+1: c+i+1] = temp_board[r-i][c-i: c+i]
        for col in range(r-i, r+i):
            temp_board[col][c-i] = temp_board[col+1][c-i]
        temp_board[r+i][c-i:c+i] = temp_board[r+i][c-i+1:c+i+1]
        for col in range(r+i, r-i, -1):
            temp_board[col][c+i] = temp_board[col-1][c+i]
        temp_board[r-i+1][c+i] = temp
    return temp_board
    # x = start[0]
    # y = start[1]
    # for
    # for i in range(x, x + length):
    #     for j in range(y, y + length):
    #         print(temp_board[i][j], temp_board[-1-i][-1-j])
    #     print(temp_board[i][y:y + length])
    #     print(temp_board[-1-i][y:y + length])


for case in check_list:
    temp_board = copy.deepcopy(board)
    for i in case:
        r = i[0]-1
        c = i[1]-1
        s = i[2]
        # start = [r-s, c-s]
        # end = [r+s, c+s]

        # length = abs(start[0] - end[0]) + 1
        # print('길이 : ', length)
        temp_board = sol(r, c, s, temp_board)
        # print(temp_board)
    for j in temp_board:
        hooah = sum(j)
        if hooah < result:
            result = hooah
print(result)
# for i in range(K):
#     r, c, s = list(map(int, sys.stdin.readline().split()))
#     start = [r-s-1, c-s-1]
#     end = [r+s-1, c+s-1]
#     print(start)
#     print(end)
