for _ in range(int(input())):
    L = []
    for i in range(int(input())):
        L.append(input())
    if ('cakewalk' not in L) or ('simple' not in L) or ('easy' not in L):
        print('No')
    elif (('easy-medium' in L) or ('medium' in L)) and (('medium-hard' in L) or ('hard' in L)):
        print('Yes')
    else:
        print('No')
