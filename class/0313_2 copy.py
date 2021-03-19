
def max_profit(day, price_list):
    cMax = price_list[day-1]                # 리스트 마지막 수 변수 선언
    profit = 0                              # 최대값 변수 선언
    for i in range(day-2, -1, -1):          # 마지막 리스트부터 루프 시작

        if cMax >= price_list[i]:           # 쵀대값보다 낮은 경우 주식을
            profit += cMax - price_list[i]  # 매도했다고 가정 수익에 더해주기
        else:
            cMax = price_list[i]            # 최대값 보다 더 큰 값이 나올경우                                                        
                                            # 최대값 갱신
    return profit                           


day = int(input())
price_list = list(map(int, input().split()))

print(max_profit(day, price_list))
