def gcd(a, b):
    if b==0:
        return a 
    return gcd(b, a%b)

for _ in range(int(input())):
    M, B = map(int, input().split())
    g = gcd(M, B)
    print(2 * g)
