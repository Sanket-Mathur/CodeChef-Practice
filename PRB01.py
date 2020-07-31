try:
    for _ in range(int(input())):
        N = int(input())
        if N == 2:
            flag = 1
        else:
            for i in range(2, N):
                if N % i != 0:
                    flag = 1
                else:
                    flag = 0
                    break
        if flag:
            print('yes')
        else:
            print('no')
except:
    pass
