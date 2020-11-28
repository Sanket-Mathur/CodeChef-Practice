for _ in range(int(input())):
    N = int(input())
    L = list(map(int, input().split()))
    fuel = L[0]
    travelled = 0
    for i in range(1,len(L)):
        if fuel == 0:
            break
        fuel += L[i] - 1 
        travelled += 1 
    print(travelled + fuel)
        
