import sys


def sol(depth):
    global answer, total
    if answer > 0 and answer <= depth:
        return

    if total == 0:
        if answer == -1 or answer > depth:
            answer = depth
        return

    for x in range(10):
        for y in range(10):
            if board[x][y] == 1:
                break
        if board[x][y] == 1:
            break

    for size in range(1, 6):
        if check[size]:
            backup = []
            if check_cover(x, y, size):
                for i in range(x, x+size):
                    for j in range(y, y+size):
                        board[i][j] = 0
                        backup.append((i, j))
                total -= (size)**2
                check[size] -= 1
                sol(depth+1)
                check[size] += 1
                total += (size)**2

                for back in backup:
                    board[back[0]][back[1]] = 1


def check_cover(x, y, size):
    for i in range(x, x+size):
        for j in range(y, y+size):
            if 0 <= i < 10 and 0 <= j < 10:
                # 0인 경우
                if board[i][j] == 0:
                    return False
            # 보드 넘어가는경우
            else:
                return False
    return True


board = [list(map(int, sys.stdin.readline().split())) for _ in range(10)]
check = [0] + [5] * 5
total = sum([sum(i) for i in board])
answer = -1

sol(0)
print(answer)
