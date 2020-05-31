for n in range(int(input())):
    s = list(map(int, input().split()))
    x = s.pop()
    tot = sum(s) * x
    if(tot <= 120):
        print('No')
    else:
        print('Yes')