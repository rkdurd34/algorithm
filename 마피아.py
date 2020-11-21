mafia = int(input())
whole = int(input())

first = [mafia, whole-mafia]
board = [[1],[1]]
for i in range(2, whole -mafia+1):
    board.append([])
    for j in range(1,i):
        board[i].append(0)
for i in range(len(board)):
    