import sys

N = int(sys.stdin.readline().strip())

for i in range(N,0,-1):
    print(' '*(i-1),'*'* (N-i+1),sep='')