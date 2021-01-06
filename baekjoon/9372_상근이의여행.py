import sys
test_case = int(sys.stdin.readline())
for i in range(test_case):
  country, air = list(map(int,sys.stdin.readline().split()))
  for j in range(air):
    num = list(map(int,sys.stdin.readline().split()))
  print(country - 1)
  

