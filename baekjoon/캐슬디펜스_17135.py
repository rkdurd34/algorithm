from itertools import combinations
import sys
import copy
N, M, D = list(map(int, sys.stdin.readline().split()))
board = []

for i in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))
check_list = list(combinations([i for i in range(M)], 3))


def sol(case, i, temp_board, D, M, check, attack_count):
    for j in range(D):
        if i - j >= 0:
            for k in range(M):
                if temp_board[i-j][k] == 1:
                    for t in case:
                        start = [N, t]
                        end = [N-j-1, k]
                        temp_distance = abs(
                            start[0]-end[0]) + abs(start[1]-end[1])
                        if check[t][0] >= temp_distance and temp_distance <= D:
                            if check[t][1] == 0:
                                check[t][1] = [i-j, k]
                                check[t][0] = temp_distance
                            else:
                                if k < check[t][1][1] and check[t][0] == temp_distance:
                                    check[t][1] = [i-j, k]
                                    check[t][0] = temp_distance
                                elif check[t][0] > temp_distance:
                                    check[t][1] = [i-j, k]
                                    check[t][0] = temp_distance
    return attack_count


attack_count = 0
for case in check_list:
    temp_board = copy.deepcopy(board)
    temp_kill_count = 0
    for i in range(N-1, -1, -1):
        check = [[float('inf'), 0] for _ in range(M)]
        sol(case, i, temp_board, D, M, check, 0)
        for a in check:
            b = a[1]
            if b != 0:
                if temp_board[b[0]][b[1]] == 1:
                    temp_board[b[0]][b[1]] = 0
                    temp_kill_count += 1

    if attack_count < temp_kill_count:
        attack_count = temp_kill_count
print(attack_count)


# # 하나의 칸에 최대 한명의 궁수
# # 각 턴마다 하나의 적만 공격 가능
# # 모든 궁수는 동시에 공격한다
# # 공격하는 적은 거리가 D이하인 적중에서 가장 가까운 적
# # 그러한 적이 여럿일경우 가장 왼쪽의 적 공격
# # 같은 적이 여러 궁수에게 당할 수 있다
# import sys

# N, M, D = list(map(int, sys.stdin.readline().split()))
# board = []

# for i in range(N):
#     board.append(list(map(int, sys.stdin.readline().split())))

# # print(N, M, D)
# # print(board)

# def kill(i, N, M, D, check, board, attack_count):
#     for j in range(D):
#         if i - j >= 0:
#             # 거리별 공격 가능 검사
#             for k in range(M):
#                 if board[i-j][k] == 1:
#                     attack_or_not = 0
#                     for t in range(len(check)):
#                         start = [M, t]
#                         end = [i-j, k]
#                         temp_distance = abs(
#                             start[0]-end[0]) + abs(start[1]-end[1])
#                         if check[t] > temp_distance:
#                             check[t] = temp_distance
#                             attack_or_not = 1
#                     if attack_or_not == 1:
#                         board[i-j][k] = 0
#                         attack_count += 1
#                 if attack_count == 3:
#                     return attack_count
#     return attack_count

# attack_count = 0
# for i in range(len(board)-1, -1, -1):
#     check = [float('inf') for _ in range(M)]
#     attack_count += kill(i, N, M, D, check, board, 0)
#     # 거리간 공격 가능 횟수
# print(attack_count)
