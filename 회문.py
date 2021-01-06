case = int(input())
def col_check(i,row):
  stack  = []
  for j in range(row//2):
    print(stack , board[j][i], board[j][-i-1])
    if board[j][i] == board[j][-i-1]:
      stack.append(board[j][i])
    else: 
      return False
  return stack

for _ in range(case):
  row, length = map(int,input().split())
  board = [ list(input()) for _ in range(row)]
  # print(board)
  for i in range(row):
    for j in range(row-length+1):
      if length % 2 == 0 and board[i][j:j+length//2] == list(reversed(board[i][j+length//2:j+length+1])):
        print(True, board[i][j:j+length//2] + board[i][j+length//2:length+1])
      elif length % 2 != 0 and board[i][j:j+length//2] == list(reversed(board[i][j+length//2+1:j+length+1])):
        print(True, board[i][j:j+length//2] +[board[i][j+length//2]] +board[i][j+length//2+1:j+length+1])
    


      
          
            



        


     