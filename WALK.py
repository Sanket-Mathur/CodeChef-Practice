for _ in range(int(input())):
    N = int(input())
    L = list(map(int, input().split()))
    speed = L[-1]
    for i in range(len(L)-2, -1, -1):
        speed += 1 
        if speed < L[i]:
            speed = L[i]
    print(speed)
