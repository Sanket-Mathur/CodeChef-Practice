for _ in range(int(input())):
    S = input()
    for i in list(set(S)):
        if S.count(i) > 1:
            print('yes')
            break
    else:
        print('no')
