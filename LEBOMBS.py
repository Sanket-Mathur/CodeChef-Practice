for _ in range(int(input())):
    N = int(input())
    S = input()
    count = 0
    for i,v in enumerate(S):
        if v == '0':
            if not ((i > 0 and S[i-1] == '1') or (i < len(S)-1 and S[i+1] == '1')):
                count += 1 
    print(count)
