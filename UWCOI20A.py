for _ in range(int(input())):
    N = int(input())
    h = int(input())
    for i in range(N-1):
        x = int(input())
        if x > h:
            h = x 
    print(h)
