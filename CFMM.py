for _ in range(int(input())):
    N = int(input())
    s = ''
    for i in range(N):
        s += input()
    c = []
    for i in list('codehf'):
        c.append(s.count(i))
    c[0] /= 2
    c[3] /= 2
    print(int(min(c)))
