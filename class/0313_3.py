def max_price():
    n = int(input())                                # 콘솔 입력 값
    price_list = list(map(int, input().split()))     # 콘솔 입력 값

    board = [0] * n                                 # 리스트 선언
    profit = 0                                      # 최대값 변수 선언
    for i in range(1, len(price_list)):
        if price_list[i-1] < price_list[i]:         # 현재값이 더 클 경우
            board[i] = board[i-1] + 1               # 최대값 갱신
            profit = max(profit, board[i])

    return profit


print(max_price())
