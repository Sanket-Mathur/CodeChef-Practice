for _ in range(int(input())):
    N, K = map(int, input().split())
    L = input().split()
    
    rem = L[:N-K]
    
    print(rem.count('T') if L[N-K]=='H' else rem.count('H'))
