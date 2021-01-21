import sys


def permutation(case, depth, amount, result, temp):
    if depth == amount:
        result.append(list(temp))
        return
    for i in range(len(case)):
        if check[i] == False:
            check[i] = True
            temp.append(case[i])
            permutation(case, depth+1, amount, result, temp)
            check[i] = False
            temp.pop()
    return result


def combination(case, depth, amount, result, index, temp):
    if depth == amount:
        result.append(list(temp))
        return
    for i in range(index, len(case)):
        if check[i] == False:
            check[i] = True
            temp.append(case[i])
            combination(case, depth+1, amount, result, i+1, temp)
            check[i] = False
            temp.pop()

    return result


case = list(map(int, sys.stdin.readline().split()))
num = int(sys.stdin.readline())

check = [False for i in range(len(case))]
permutation_result = permutation(case, 0, num, [], [])
combination_result = combination(case, 0, num, [], 0, [])
print(combination_result)
print(permutation_result)
