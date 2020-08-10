try:
    for _ in range(int(input())):
        N = int(input())
        C = list(input())
        l = [C.count('R'), C.count('G'), C.count('B')]
        print(sum(l) - max(l))
except:
    pass
