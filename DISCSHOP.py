for _ in range(int(input())):
    N = list(input())
    for i in range(len(N)-1):
        if N[i] > N[i+1]:
            del N[i]
            print(int(''.join(N)))
            break
    else:
        print(int(''.join(N[:-1])))
