try:
    for _ in range(int(input())):
        N = int(input())
        s = list(input())
        for i in range(0, len(s)-1, 2):
            s[i],s[i+1] = s[i+1],s[i]
        for i in range(len(s)):
            s[i] = chr(122 - ord(s[i]) + 97)
        print(*s, sep='')
except:
    pass
