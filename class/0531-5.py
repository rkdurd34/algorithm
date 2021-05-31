import sys
m = int(sys.stdin.readline())
board = {}
check = {}
for _ in range(m):
    n, u, v = list(sys.stdin.readline().strip().split())
    # 이중 딕셔너리 구조로 데이터 저장
    if u not in board.keys():
        board[u] = dict()
        board[u][v] = n
    else:
        board[u][v] = n
    if v not in board.keys():
        board[v] = dict()
        board[v][u] = n
    else:
        board[v][u] = n
    check[u] = False # 방문 유무 검사
    check[v] = False
# 출발지, 목적지
a, b = sys.stdin.readline().strip().split()


def BFS(board, a, b):
    # [호선 , 환승횟수, 지나온 역]
    need_visit = [[0, 0, a]]
    result = []
    check[a] = True # 방문 체크
    while need_visit:
        # 뎁스별 임시 리스트
        temp_list = []
        for i in range(len(need_visit)):
            for j, k in board[need_visit[i][-1]].items():
                temp = list(need_visit[i])
                # 마지막으로 거쳐온 호선
                last_hosun = temp[0]
                # 방문하지 않은 경우
                if check[j] == False:
                    # 환승한 경우 환승횟수 증가 및 호선 변경
                    if last_hosun != k:
                        temp[1] += 1
                        temp[0] = k
                    # 리스트에 지나온 역 추가
                    temp.append(j)
                    if j == b:
                        # 목적지에 도착한 경우 결과 값에 추가 및 다음 노드로 스킵
                        result.append(temp)
                        continue
                    # 환승횟수, 호선, 지나온역이 갱신된 노드 임시 리스트에 추가
                    temp_list.append(temp)
        # 한 뎁스 내에서 같은 노드를 또 방문 할 수 있으므로 
        # 한 뎁스 탐색이 모두 끝 마친 이후에 노드들 방문 처리!!!
        for i in range(len(need_visit)):
            check[need_visit[i][-1]] = True
        # 방문 해야 할 리스트 갱신
        need_visit = list(temp_list)
        # 결과값의 길이가 0보다 크면 목적지에 도달함
        if len(result) > 0:
            # 환승횟수가 제일 적은 경로를 뽑아내기
            result = min(result, key=lambda x: (len(x), x[1]))[2:]
            print(len(result))
            print(*result)
            return
    # 목적지에 도달하지 못한경우
    print(-1)
    return


BFS(board, a, b)
