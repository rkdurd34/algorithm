
import sys
from itertools import permutations
case = int(sys.stdin.readline())


def sol(num):
    num_list = [1, 2, 3]
    board = [set(["1"]), set(["2"]), set(["3"])] + [set()
                                                    for i in range(num-1)]
    for i in range(len(board)-3):
        for j in board[i]:
            for k in range(1, 4):
                board[i+k].add(j+str(k))
                board[i+k].add(str(k)+j)

    print(len(board[-3]))
    # print(board)


for i in range(case):
    num = int(sys.stdin.readline())
    result = sol(num)
