import sys

T = int(sys.stdin.readline().strip())

for _ in range(T):
    A, B = map(int,sys.stdin.readline().split())
    print(A+B)