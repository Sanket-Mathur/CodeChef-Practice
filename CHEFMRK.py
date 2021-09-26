from sys import stdin, stdout

l = [int(stdin.readline().strip()) for i in range(3)]
stdout.write(f'{sorted(l)[1]}\n')