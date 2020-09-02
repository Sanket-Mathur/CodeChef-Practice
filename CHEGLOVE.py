for _ in range(int(input())):
    N = int(input())
    Fin = list(map(int, input().split()))
    Glo = list(map(int, input().split()))
    front = back = True
    for i in range(0,N):
        if Fin[i] > Glo[i]:
            front = False
        if Fin[i] > Glo[N-i-1]:
            back = False
    if front and back:
        print('both')
    elif front:
        print('front')
    elif back:
        print('back')
    else:
        print('none')
