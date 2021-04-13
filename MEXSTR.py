from sys import stdin, stdout

def isSubsequence(x, y):
    it = iter(y)
    return all(any(c == ch for c in it) for ch in x)
    
for i in range(int(stdin.readline())):
    S = '0b' + stdin.readline()
    i = 0
    while isSubsequence(bin(i), S):
        i += 1 
    stdout.write(f'{bin(i)[2:]}\n')
