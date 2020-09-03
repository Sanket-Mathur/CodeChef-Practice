for _ in range(int(input())):
    N = int(input())
    S = list(input())
    for i in set(S):
        if S.count(i) % 2:
            print('NO')
            break
    else:
        print('YES')
