import sys

N = int(sys.stdin.readline().strip())
print('\n'.join([f"{N} * {i} = {N * i}" for i in range(1,10)]))