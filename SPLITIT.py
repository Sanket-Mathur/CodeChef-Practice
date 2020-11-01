for _ in range(int(input())):
    N = int(input())
    S = input()
    print('YES' if S[:-1].count(S[-1]) > 0 else 'NO')
