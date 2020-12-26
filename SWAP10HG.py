for _ in range(int(input())):
    N = int(input())
    S1 = input()
    S2 = input()
    if S1 == S2:
        print('Yes')
    else:
        ones = 0
        for i in range(N):
            if S1[i] != S2[i]:
                if S1[i] == '1':
                    ones += 1 
                else:
                    ones -= 1 
            if ones < 0:
                print('No')
                break
        else:
            if ones == 0:
                print('Yes')
            else:
                print('No')
