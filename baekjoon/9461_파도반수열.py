n = int(input())
if n == 0:
  print(0)
check = [int(input()) for _ in range(n)]
board = [1,1,1]+[0 for i in range(100)]
for j in check:
  if j == 1 or j==2:
    print(1)
  else:
    for i in range(2,j):
      board[i] = board[i-2]+ board[i-3]
    print(board[j-1]) 


    
