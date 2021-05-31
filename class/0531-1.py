import sys
m, n = list(map(int, sys.stdin.readline().split()))
board = []
start = []
for i in range(m):
    temp = list(map(int, sys.stdin.readline().strip()))
    board.append(temp) # 이중리스트로 인접리스트 구현
    if i == 0: # 출발 가능한 맨윗라인 스택에 추가
        for j in range(len(temp)):
            if temp[j] == 1: 
                start.append([0, j])


def DFS(board, m, n, start):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    while start:
        x, y = start.pop() # 스택에서 하나씩 빼기
        for i in range(len(dx)):  
            new_x, new_y = x+dx[i], y+dy[i]
            if 0 <= new_x < m and 0 <= new_y < n: # 가능한 지역 검사
                if board[new_x][new_y] == 1: # 방문 가능 조건
                    if new_x == m-1: # 맨아랫선 방문시 종료
                        print(1)
                        return
                    start.append([new_x, new_y]) # 다음 방문을 위해 추가
                    board[new_x][new_y] = 0 # 방문 표시
    print(-1) # 맨안래 방문 못할시 -1 출려
    return


DFS(board, m, n, start)
