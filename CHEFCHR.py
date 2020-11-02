for _ in range(int(input())):
    S = input()
    c = 0
    for i in range(len(S)-3):
        if sorted(S[i:i+4]) == ['c','e','f','h']:
            c += 1
    print('lovely ' + str(c) if c else 'normal')
