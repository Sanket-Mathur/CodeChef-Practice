for _ in range(int(input())):
    S = input()
    possible = 1
    start, end = 0, len(S)-1
    flag = True
    while start <= end:
        if S[start] == '?' and S[end] == '?':
            possible = (possible * 26) % 10000009
        elif S[start] != '?' and S[end] != '?' and S[start] != S[end]:
            print(0)
            flag = False
            break
        start += 1 
        end -= 1
    if flag:
        print(possible)
