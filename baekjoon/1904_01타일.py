n = int(input())
def solution(n):
  answer = 0
  if n == 1:
    answer = 1
    return answer
  elif n == 2:
    answer = 2
    return answer
  check = [1,2]+[100001 for _ in range(1000001)]
  for i in range(2,n):
      check[i] = (check[i-2] + check[i-1])%15746
  answer = check[n-1]
  return answer
answer = solution(n)
print(answer)