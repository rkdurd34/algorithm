def factorial_1(n):
    fac = 1
    for index in range(2,n+1):
        fac = fac *index
    return fac
answer = factorial_1(3)
print(answer)
def factorial_2(n):
    if n > 1:
        return n * factorial_2(n-1)
    else:
        return 1

# 알고리즘 성능 표기법
# O표기법은 알고리즘의 최악의 성능을 표시
# 가장 많이/일반적으로 사용함
# 아무리 최악의 상황이라도, 이정도의 성능은 보장한다는 의미이기 때문
# Ω표기법은 알고리즘의 최고의 성능을 표시
# θ표기법은 정확한 알고리즘의 성능을 표시
# 대문자 O 표기법
# 빅 오 표기법이라고도 부름
# O(입력)
# 입력 n 에 따라 결정되는 시간 복잡도 함수
# O(1), O(logn), O(n), O(nlogn), O(n2), O(2n), O(n!)등으로 표기함
# 입력 n 의 크기에 따라 기하급수적으로 시간 복잡도가 늘어날 수 있음
# O(1) < O(logn) < O(n) < O(nlogn) < O(n2) < O(2n) < O(n!)
def add_all_1(n):
    num =0
    for i in range(1,n+1):
        num+=i
    return num
print(add_all_1(100))
def add_all_2(n):
    return int(n*(n+1)/2)
print(add_all_2(100))
names = ['dave','david','anthony','david','dave']
same_name = []
for i in names:
    if i not in same_name:
        same_name.append(i)
print(same_name)
def find_same_name(name_list):
    for index, name in enumerate(name_list):
        for index2 in range(index+1, len(name_list)):
            if (name == name_list[index2]):
                del name_list[index2]
                print(name_list)
    return name_list
print(find_same_name(names))


