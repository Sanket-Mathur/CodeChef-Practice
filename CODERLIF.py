try:
    for _ in range(int(input())):
        L = list(map(int, input().split()))
        c = 0
        for i in L:
            if i == 1:
                c += 1
                if c > 5:
                    print('#coderlifematters')
                    break
            else:
                c = 0
        else:
            print('#allcodersarefun')
except:
    pass
