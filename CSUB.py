for t in range(int(input())):

    N = int(input())
    S = list(input())
    n = S.count('1')

    print(int((n/2) * (2 + (n-1)))) # Sum of AP