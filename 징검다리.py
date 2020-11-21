num_input = int(input())
board = list(map(int,input().split()))

check = [False ] * (num_input+100)
check[0] =True
def sol(board,check):
    answer = False
    present = 0 
    check_list = [0]
    while check_list:
        temp_list = set()
        for i in range(len(check_list)):
            if check_list[i] == len(board)-1:
                return True
            for j in range(board[check_list[i]]):
                if check_list[i]+j+1 <= len(board)-1 :
                    if check[check_list[i]+j+1]==False:
                        temp_list.add(check_list[i]+j+1)
                        check[check_list[i]+j+1] = True
        check_list = list(temp_list)
    return False
a = sol(board,check)
print(a)
        
