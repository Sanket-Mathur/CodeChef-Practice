for i in range(int(input())):
    N = int(input())
    s = 'zyxwvutsrqponmlkjihgfedcba'
    r = ''
    while True:
        r = s[-N-1:] + r  
        if N < 26:
            break
        N -= 25
    print(r)
