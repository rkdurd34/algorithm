n=1000
prime = True
i = 2
while i*i <= n:
    if n % i == 0:
        prime = False
        break
    i += 1

if prime:
    print("Prime")
else:
    print('not prime')

n=1000
a = [False,False] + [True]*(n-1)
primes=[]

for i in range(2,n+1):
  if a[i]:
    primes.append(i)
    for j in range(2*i, n+1, i):
        a[j] = False
print(primes)