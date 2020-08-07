try:
    def prod(l):
        p = 1
        for i in l:
            p *= i 
        return p
    for _ in range(int(input())):
        N = int(input())
        L = list(map(int, input().split()))
        c = 0
        for i in range(N):
            for j in range(i,N):
                if sum(L[i:j+1]) == prod(L[i:j+1]):
                    c += 1 
        print(c)
except:
    pass
