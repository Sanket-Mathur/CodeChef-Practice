try:
    for _ in range(int(input())):
        L = input().split(' ')
        if len(L) > 1:
            print(*[L[i][0].upper() + '.' for i in range(len(L)-1)], end=' ')
        print(L[-1].title())
except:
    pass
