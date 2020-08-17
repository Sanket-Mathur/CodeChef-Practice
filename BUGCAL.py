try:
    for _ in range(int(input())):
        A, B = map(int, input().split())
        s = 0
        for i in range(max(len(str(A)), len(str(B)))):
            a = A % 10
            b = B % 10
            s += ((a+b) % 10) * 10**i 
            A //= 10
            B //= 10
        print(s)
except:
    pass
