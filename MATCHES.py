try:
    L = [6,2,5,5,4,5,6,3,7,6]
    for _ in range(int(input())):
        A, B = map(int, input().split())
        res = A + B 
        s = 0
        for i in list(str(res)):
            s += L[int(i)]
        print(s)
except:
    pass
