
def BFS(board, a, b, n):
		visited = [False] * n # 방문 여부 리스트
		visited[a] = True # 방문 체크 리스트
		count = 0 # 뎁스 구분
		need_visit = board[a] # 방문 필요 리스트 초기화
		while need_visit:
				temp_list = [] # 뎁스 구분을 위한 임시 리스트
				for i in range(len(need_visit)): 
						temp = need_visit[i] # 방문시작
						if visited[temp] == False:
								if temp == b:
										print(count+1) # 목적지 도착시 종료
										return
								temp_list.extend(board[temp]) # 방문 후 임시리스트에 추가
								visited[temp] = True # 방문 표시
				count += 1 # 뎁스 카운트 추가
				need_visit = list(temp_list) # 방문 필요 리스트 임시리스트로 대체
		print(-1) # 목적지 도달 못할시 -1 출력
		return


import sys
n,m = list(map(int,sys.stdin.readline().strip()))

board = [[] for _ in range(n)]
for i in range(m): # 이중리스트로 인접리스트 생성
		u, v = list(map(int, sys.stdin.readline().split()))
		board[u].append(v)
		board[v].append(u)
a, b = list(map(int, sys.stdin.readline().split()))


BFS(board, a, b, n)


  