day = int(input())                                      # 콘솔 입력 값
price_list = list(map(int, input().split()))            # 콘솔 입력 값

board = [[price_list[0], price_list[0], price_list[0]]] # DP를 위한 초기값 세팅
                                                        # 구매가, 판매가, 이전 구매가보다 낮은 구매가 보관
for i in range(1, day):
    check = price_list[i]                               # 변수 선언
    bought_price = board[i-1][0]                        # 변수 선언
    sold_price = board[i-1][1]                          # 변수 선언
    low_price = board[i-1][2]                           # 변수 선언
    temp_list = list(board[i-1])                        # 다음 DP를 위한 이전 DP 복제
    post_total = sold_price - bought_price              # 변수선언
    if post_total < check - low_price:                  # 이전 합보다 현재 합(보관된 구매가)
        temp_list[0] = low_price                        # 이 더 작을시 리스트 업데이트
        temp_list[1] = check
    if post_total == check - low_price:
        if low_price < bought_price:                    # 이전 합과 같지만 가격이 더 낮은 경우
            temp_list[0] = low_price                    # 리스트 업데이트
            temp_list[1] = check

    if post_total < check - bought_price:               # 이전 합보다 현재 합(이전 구매가)이
        temp_list[1] = check                            # 더 작을시 리스트 업데이트
    if post_total == check - bought_price:              # 이전 합과 같지만
        if bought_price > check:                        # 구매가가 더 작은경우 리스트 업데이트
            temp_list[0] = check
    if check < low_price:                               # 이전 구매가보다 새로운 구매가가
        temp_list[2] = check                            # 더 작을시 보관 구매가 업데이트

    board.append(temp_list)                             # DP리스트 업데이트

result = board[-1]
if result[1] - result[0] <= 0:                          # 이익이 0인 경우 -1 출력
    print(-1)                                           # 이익이 0 초과일 경우
else:                                                   # 이익과, 가격 출력
    print(result[1]-result[0])
    print(result[0], result[1])

