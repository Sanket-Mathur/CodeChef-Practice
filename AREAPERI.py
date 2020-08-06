try:
    l = int(input())
    b = int(input())
    if l*b == 2*(l+b):
        print('Eq')
        print(l*b)
    elif l*b > 2*(l+b):
        print('Area')
        print(l*b)
    else:
        print('Peri')
        print(2*(l+b))
except:
    pass
