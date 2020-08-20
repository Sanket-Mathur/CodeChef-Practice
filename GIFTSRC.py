try:
    def move(M, l):
        if M == 'L':
            l[0] = l[0]-1
        elif M == 'R':
            l[0] = l[0]+1
        elif M == 'U':
            l[1] = l[1]+1
        elif M == 'D':
            l[1] = l[1]-1
    def inva(M):
        if M == 'U': return 'D'
        elif M == 'D': return 'U'
        elif M == 'L': return 'R'
        else: return 'L'
    for _ in range(int(input())):
        N = int(input())
        S = input()
        l = [0,0]
        move(S[0], l)
        for i in range(1,len(S)):
            if S[i] != S[i-1] and S[i] != inva(S[i-1]):
                move(S[i],l)
        print(*l)
except:
    pass
