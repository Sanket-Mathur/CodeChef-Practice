from math import gcd

for _ in range(int(input())):
    N, A, B, K = map(int, input().split())
    a = N // A
    b = N // B
    lcm = (A*B) // gcd(A,B)
    c = N // lcm
    solvable = a + b - 2*c
    print('Win' if solvable >= K else 'Lose')
