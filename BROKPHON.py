for _ in range(int(input())):
    N = int(input())
    L = list(map(int, input().split()))
    last = 0
    cnt = set()
    for i in range(len(L)):
        if L[i] != L[last]:
            cnt.add(i)
            if i > 0:
                cnt.add(i-1)
            cnt.add(i-1)
            last = i
    print(len(cnt))
