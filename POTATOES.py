try:
    def isprime(n):
        if n < 2:
            return False
        elif n == 2:
            return True
        else:
            for i in range(2,n):
                if n % i == 0:
                    return False
            return True
    for _ in range(int(input())):
        x, y = map(int, input().split())
        i = 1 
        while not isprime(x+y+i):
            i += 1 
        print(i)
except:
    pass
