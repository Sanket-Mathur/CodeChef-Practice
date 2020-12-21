for _ in range(int(input())):
    S = input()
    if len(S) % 2:
        print(-1)
    else:
        ones = S.count('1')
        zeros = S.count('0')
        if ones == 0 or zeros == 0:
            print(-1)
        else:
            print(abs(ones - zeros) // 2)
