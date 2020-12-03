for _ in range(int(input())):
    N, P = input().split()
    N = int(N)
    Heap = list(map(int, input().split()))
    if N == 1 and P == 'Dee' and Heap[0]%2==0:
        print('Dee')
    else:
        print('Dum')
