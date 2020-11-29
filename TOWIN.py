for _ in range(int(input())):
    N = int(input())
    L = sorted(map(int, input().split()), reverse=True)
    temp = L.pop(2) if len(L) > 2 else 0
    first, second = sum(L[::2]), sum(L[1::2])+temp
    if first == second:
        print('draw')
    else:
        print('first' if first>second else 'second')
