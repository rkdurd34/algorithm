hash_table = list([i for i in range(10)])
print(hash_table)
data1 = "Andt"
data2 = "Dave"
data3 = "Trump"
data4 = "Anthor"
def hash_func(key):
    return key%5
print(ord(data1[0]), ord(data2[0]), ord(data3[0]))
print(ord(data1[0]), hash_func(ord(data1[0])))