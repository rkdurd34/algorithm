a,b = map(int,input().split())
t = []
ditac = [False] * a
result = []
def solve(depth, a, b):
    if depth == b:
        print(result)
    for i in range(len(ditac)):
        t.append(1)
        print(len(t))
        if ditac[i] == False:
            ditac[i] = True
            result.append(i+1)
            solve(depth+1,a ,b)
            ditac[i] = False
            result.pop()
    
                

solve(0,a,b)

