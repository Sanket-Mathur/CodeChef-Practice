# Partially Accepted
try:
    for _ in range(int(input())):
    
        S = sorted(input().strip())
        P = input().strip()
        
        dic = {i: S.count(i) - P.count(i) for i in set(S)}
        ans = [i * dic[i] for i in dic.keys() if dic[i]>0] 
        ans.append(P)
        print(''.join(sorted(ans)))
    
except:
    pass
