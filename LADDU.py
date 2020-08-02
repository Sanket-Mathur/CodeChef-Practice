try:
    for _ in range(int(input())):
        N, origin = input().split()
        N = int(N)
        l = 0
        for n in range(N):
            act = input()
            if act[:11] == 'CONTEST_WON':
                l += 300
                rank = int(act[12:])
                if rank < 20:
                    l += 20-rank
            elif act == 'TOP_CONTRIBUTOR':
                l += 300
            elif act[:9] == 'BUG_FOUND':
                sev = int(act[10:])
                l += sev
            else:
                l += 50
        if origin == 'INDIAN':
            print(l // 200)
        else:
            print(l // 400)
except:
    pass
