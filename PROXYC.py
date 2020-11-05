import math

for _ in range(int(input())):
    N = int(input())
    S = list(input())
    Cp = S.count('P')
    Ca = S.count('A')
    req = math.ceil(N * 0.75)
    if req <= Cp:
        print(0)
    else:
        c = 0
        for i in range(2,N-2):
            if (S[i]=='A') and (S[i-1]=='P' or S[i-2]=='P') and (S[i+1]=='P' or S[i+2]=='P'):
                c += 1 
        print(req-Cp if Cp+c>=req else -1)
