import sys
n = int(sys.stdin.readline())
# word_list = ['i', 'im', 'it', 'no', 'no', 'but', 'more', 'more', 'wait', 'wont', 'yours', 'cannot', 'hesitate']
word_list=[]
for i in range(n):
    word_list.append(sys.stdin.readline()[:-1])
word_list = set(word_list)
word_list = list(word_list)
word_list_sort = sorted(word_list, key = lambda x:(len(x), x[:]))
for i in word_list_sort:
    print(i)


