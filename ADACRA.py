try:
    for _ in range(int(input())):
        C = list(input())
        i = 1 
        while i < len(C):
            if C[i] == C[i-1]:
                del C[i]
            else:
                i += 1
        print(min(C.count('U'), C.count('D')))
except:
    pass
