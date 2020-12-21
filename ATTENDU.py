for _ in range(int(input())):
    N = int(input())
    leaves = input().count('0')
    if 120 - leaves >= 90:
        print('YES')
    else:
        print('NO')
