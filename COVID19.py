for _ in range(int(input())):
    N = int(input())
    L = sorted(map(int, input().split()))
    inf = []
    for i in range(N):
        infected = 1
        left = right = i
        while left > 0 and L[left]-L[left-1] <= 2:
            left -= 1 
            infected += 1 
        while right < N-1 and L[right+1]-L[right] <= 2:
            right += 1 
            infected += 1 
        inf.append(infected)
    print(min(inf), max(inf))
