for T in range(int(input())):

    N = int(input())
    S = list(map(int, input().split()))
    S.sort()

    m = abs(S[0]-S[1])

    for i in range(len(S)-1):
        x = abs(S[i] - S[i+1])
        if x < m:
            m = x
    
    print(m)