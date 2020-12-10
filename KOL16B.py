def decodeInteger(a):
    return a & ((1 << 16) - 1), a >> 16 

for t in range(int(input())):
    N = int(input())
    A, B = [], []
    for n in range(N):
        a = int(input())
        a, b = decodeInteger(a)
        A.append(a)
        B.append(b)
    print('Case {}:'.format(t + 1))
    print(*A)
    print(*B)
