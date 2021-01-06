num_input = int(input())

def sol(num_input):
  
  if num_input<=20:
    dp = [[[1,3]], [[1,2],[1,3],[2,3]]] + [[] for _ in range(2,num_input)]
    for i in range(2, len(dp)):
      dp[i].extend(dp[i-2])
      for j in range(len(dp[i]), len(dp[i-1])):
        temp = [dp[i-1][j][0],dp[i-1][j][1]]
        for t in range(2):
          if dp[i-1][j][t] ==3:
            temp[t] = 2
          if dp[i-1][j][t] ==2:
            temp[t] = 3
        # if dp[i-1][j][0] == 3:
        #   temp[0] = 2
        # if dp[i-1][j][0] == 2:
        #   temp[0] = 3
        # if dp[i-1][j][1] == 3:
        #   temp[1] = 2
        # if dp[i-1][j][1] == 2:
        #   temp[1] = 3
        dp[i].append(temp)
      dp[i].append([1,3])
      for k in range(len(dp[i-1])):
        temp = [dp[i-1][k][0], dp[i-1][k][1]]
        for t in range(2):
          if dp[i-1][k][t] ==1:
            temp[t] = 2
          if dp[i-1][k][t] ==2:
            temp[t] = 1
        # if dp[i-1][k][0] == 1:
        #   temp[0] =2
        # if dp[i-1][k][0] == 2:
        #   temp[0] =1
        # if dp[i-1][k][1] == 1:
        #   temp[1] =2
        # if dp[i-1][k][1] == 2:
        #   temp[1] =1
        dp[i].append(temp)
    print(len(dp[-1]))
    for i in dp[-1]:
      print(*i)
  else:
    dp = [1,3] + [0 for _ in range(2,num_input)]
    for i in range(2,len(dp)):
      dp[i] = (dp[i-1] * 2) + 1
    print(dp[-1])
sol(num_input)
  