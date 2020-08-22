try:
    for _ in range(int(input())):
        N = int(input())
        S1 = input()
        S2 = input()
        if S1.count('1') == S2.count('1'):
            print('YES')
        else:
            print('NO')
except:
    pass
