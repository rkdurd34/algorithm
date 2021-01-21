import sys
sys.setrecursionlimit(10**8)
result = set()
a = [5, 6, 7, 8, 9]
b = [1, 2, 3, 4]
c = [2, 4, 6, 8]
board = [a, b, c]
check = [False, False, False]


def dfs(temp):
    if len(temp) == 3:
        result.add("".join(list(map(str, temp))))
        return
    for i in range(len(check)):
        if check[i] == False:
            check[i] = True
            for j in range(len(board[i])):
                temp.append(board[i][j])
                dfs(temp)
                temp.pop()
            check[i] = False
    return


dfs([])
result = list(result)
result.sort()
print(result, len(result))
