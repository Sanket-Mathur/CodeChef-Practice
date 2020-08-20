from math import sqrt
try:
    A = int(input())
    B = int(input())
    C = int(input())
    print(((-B)+sqrt(B**2-4*A*C)) / (2*A))
    print(((-B)-sqrt(B**2-4*A*C)) / (2*A))
except:
    pass
