def gcd(a, b):
    if b == 0:
        return a 
    return gcd(b, a%b)

def lcm(a, b):
    return (a*b) // gcd(a,b)

for _ in range(int(input())):
    N = int(input())
    L = list(map(int, input().split()))
    min_lcm = -1
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            l = lcm(L[i], L[j])
            if l < min_lcm or min_lcm == -1:
                min_lcm = l 
    print(min_lcm)
