# num = 2143

# def strange_sort(strings,n):
#     return sorted(strings,key=lambda strings:strings[n])
# print(strange_sort(['sun','bed','car'],1))

# check_score = lambda x:'pass' if x>= 60 else "fail"
# print(check_score(70))
import sys
n = input()
a = [int(sys.stdin.readline()) for i in range(int(n))]
print(a)
num = input()
num_list = list(map(int,num))
num_list.sort(reverse=True)
num_list = list(map(str,num_list))
print("".join(num_list))
