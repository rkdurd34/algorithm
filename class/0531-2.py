import sys
m, n = list(map(int, sys.stdin.readline().split()))
board = []
start = []
for i in range(m):
    temp = list(map(int, sys.stdin.readline().strip()))
    board.append(temp) # 이중리스트로 인접리스트 구현
    if i == 0:
        for j in range(len(temp)):
            if temp[j] == 1: # 맨윗라인 출발 지점 추가
                start.append([0, j])


def BFS(board, m, n, start):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    count = 1 # 뎁스구분
    while start:
        temp_list = [] # BFS 1 뎁스를 위한 리스트
        for temp in start: # 1뎁스 실행
            x, y = temp
            for i in range(len(dx)):
                new_x, new_y = x+dx[i], y+dy[i]
                if 0 <= new_x < m and 0 <= new_y < n: # 방문 가능지역검사
                    if board[new_x][new_y] == 1:
                        if new_x == m-1: # 맨아래 방문시 종료
                            print(count+1) 
                            return
                        temp_list.append([new_x, new_y]) # 다음 방문 위해 추가
                        board[new_x][new_y] = 0 # 방문 표시
        count += 1 # 뎁스 추가
        start = temp_list # 방문 필요 리스트 바꾸기
    print(-1)
    return


BFS(board, m, n, start)
