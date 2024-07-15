import sys

X = int(sys.stdin.readline().strip())
N = int(sys.stdin.readline().strip())


for _ in range(N):
    a, b = map(int,sys.stdin.readline().split())
    X -= a*b

print('Yes' if X == 0 else 'No')