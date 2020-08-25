try:
    for _ in range(int(input())):
        N = int(input())
        L = [1 if i=='cookie' else 0 for i in input().split(' ')]
        for i in range(N):
            if L[i]==1 and (i==N-1 or L[i+1]!=0):
                print('NO')
                break
        else:
            print('YES')
except:
    pass
