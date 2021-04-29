from sys import stdin, stdout
from math import sqrt

for _ in range(int(stdin.readline())):
    p, s = map(int, stdin.readline().split())
    v = (((p - (sqrt((p ** 2) - (24 * s)))) / 12) ** 2) * ((p / 4) - 2 * ((p - sqrt((p ** 2) - (24 * s))) / 12))
    stdout.write('{:.2f}\n'.format(v))
