for _ in range(int(input())):
    S = input().strip()
    i, j = 0, len(S)-1
    count = 0
    while i < j:
        if S[i] != S[j]:
            count += abs(ord(S[i]) - ord(S[j]))
        i += 1 
        j -= 1 
    print(count)
