try:
    for _ in range(int(input())):
        s = input()
        c = 0
        if s[0] != s[-1]: c = 1
        for i in range(1,len(s)):
            if s[i] != s[i-1]:
                c += 1 
        print('uniform' if c <= 2 else 'non-uniform')
except:
    pass
