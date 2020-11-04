a = list(range(1,1000001))
for i in range(1,1000000):
    a[i] = (a[i] + a[i-1] + a[i]*a[i-1]) % 1000000007
    
for _ in range(int(input())):
    print(a[int(input()) - 1])
