N = int(input())
d = int(input(), 2)
c = 0
while d % 2 == 0:
    d //= 2
    c += 1 
print(c)
