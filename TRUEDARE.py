for _ in range(int(input())):
    tr = int(input())
    Tr = set(map(int, input().split()))
    dr = int(input())
    Dr = set(map(int, input().split()))
    ts = int(input())
    Ts = set(map(int, input().split()))
    ds = int(input())
    Ds = set(map(int, input().split()))
    if len(Tr.intersection(Ts)) == len(Ts) and len(Dr.intersection(Ds)) == len(Ds):
        print('yes')
    else:
        print('no')
