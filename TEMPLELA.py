try:
    for _ in range(int(input())):
        N = int(input())
        L = list(map(int, input().split()))
        if L[0] != 1 or L[-1] != 1:
            print('no')
        else:
            for i in range(1,len(L)):
                if (i < len(L)//2 + 1) and (L[i] != L[i-1] + 1):
                    print('no')
                    break
                if (i >= len(L)//2 + 1) and (L[i] != L[i-1] - 1):
                    print('no')
                    break
            else:
                print('yes')
except:
    pass
