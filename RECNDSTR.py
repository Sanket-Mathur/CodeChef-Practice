def Left(S):
    temp = S[0]
    for i in range(len(S)-1):
        S[i] = S[i+1]
    S[-1] = temp
    return S
    
def Right(S):
    temp = S[-1]
    for i in range(len(S)-1, 0, -1):
        S[i] = S[i-1]
    S[0] = temp
    return S

for _ in range(int(input())):
    S = input()
    l = Left(list(S))
    r = Right(list(S))
    print('YES' if l == r else 'NO')
