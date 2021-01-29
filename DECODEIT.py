for _ in range(int(input())):
    N = int(input())
    S = input()
    for i in range(0, N, 4):
        print(chr(97 + int(S[i:i+4], 2)), end='')
    print('')
