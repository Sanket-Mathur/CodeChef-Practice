try:
    for _ in range(int(input())):
        N = int(input())
        S = input()
        vowels = ('a','e','i','o','u')
        count = 0
        for i in range(1,len(S)):
            if S[i] in vowels and S[i-1] not in vowels:
                count += 1
        print(count)
except:
    pass
