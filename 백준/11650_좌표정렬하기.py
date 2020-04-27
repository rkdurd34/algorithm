num = int(input())
dot_case = []
for i in range(num):
    dot_case.append(list(map(int,input().split())))
    print(dot_case)
    a = input()
    # dot_list = a.split(' ')
    # dot_case.append(dot_list)
dot_case_sort = sorted(dot_case, key = lambda x: (x[0], x[1]) )
for [i,j] in dot_case_sort:
    # for 문 돌릴 때 리스트 형식으로 포문 돌릴 수 있다!!!! 대박
    print(i,j)

# a = [(1, 2), (0, 1), (5, 1), (5, 2), (3, 0)]

# # 인자없이 그냥 sorted()만 쓰면, 리스트 아이템의 각 요소 순서대로 정렬을 한다.
# b = sorted(a)
# # b = [(0, 1), (1, 2), (3, 0), (5, 1), (5, 2)]

# # key 인자에 함수를 넘겨주면 해당 함수의 반환값을 비교하여 순서대로 정렬한다.
# c = sorted(a, key = lambda x : x[0])
# # c = [(0, 1), (1, 2), (3, 0), (5, 1), (5, 2)]
# d = sorted(a, key = lambda x : x[1])
# # d = [(3, 0), (0, 1), (5, 1), (1, 2), (5, 2)]

# # 아이템 첫 번째 인자를 기준으로 오름차순으로 먼저 정렬하고,
# # 그리고 그 안에서 다음 두 번째 인자를 기준으로 내림차순으로 정렬하게 하려면, 다음과 같이 할 수 있다.
# e = [(1, 3), (0, 3), (1, 4), (1, 5), (0, 1), (2, 4)]
# f = sorted(e, key = lambda x : (x[0], -x[1]))
# # f = [(0, 3), (0, 1), (1, 5), (1, 4), (1, 3), (2, 4)]
# 정리하면,

# sorted()의 key 인자로, 내가 커스텀할 비교 함수를 보내주면 넣어주면 된다.
# 비교 함수는 비교할 아이템의 요소를 반환하면 된다.
# 비교 함수는 익명 함수(lambda) 도 가능하고, 별도로 정의해도 된다.
# 비교할 아이템의 요소가 복수 개일 경우, 튜플로 그 순서를 내보내주면 된다.
# ex. sorted(e, key = lambda x : (x[0], -x[1]))
# -를 붙이면, 현재 정렬차순과 반대로 하게 된다.
# 한 번 정리해두면, 여기저기 잘 써먹을 수 있으므로, 잘 익혀둬야겠다.



# 출처: https://dailyheumsi.tistory.com/67 [하나씩 점을 찍어 나가며]
