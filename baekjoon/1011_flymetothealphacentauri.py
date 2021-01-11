import sys
case = int(sys.stdin.readline())
for i in range(case):
    start, end = list(map(int, sys.stdin.readline().split()))
    print(start, end)
