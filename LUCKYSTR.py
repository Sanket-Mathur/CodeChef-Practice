K, N = map(int, input().split())
luckysub = []
for i in range(K):
    luckysub.append(input())

for i in range(N):
    S = input()
    if len(S) >= 47:
        print('Good')
    else:
        for i in luckysub:
            if S.find(i) >= 0:
                print('Good')
                break
        else:
            print('Bad')
