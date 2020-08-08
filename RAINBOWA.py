try:
    for _ in range(int(input())):
        N = int(input())
        L = list(map(int, input().split()))
        i, j = 0, N-1
        flag = True if L[i] == 1 else False
        while(i < j):
            if L[i] != L[j]:
                flag = False
                break
            if L[i] != L[i+1] and L[i]+1 != L[i+1]:
                flag = False
                break
            i += 1; j -= 1 
        if L[i] != 7:
            flag = False
        
        if flag:
            print('yes')
        else:
            print('no')
except:
    pass
