import sys
M, e, d, n = list(map(int, sys.stdin.readline().split()))


def sol_1(a, k, n):
    if k == 1:                          # 1인 경우
        return (a ** k) % n     
    elif k % 2 == 0:                    # 홀수인 경우
        return ((a**(2//k)) ** 2) % n
    elif k % 2 == 1:                    # 짝수인 경우
        return (a * (a**(k-1) % n)) % n


a = sol_1(M, e, n)
print(a)
print(sol_1(a, d, n))
