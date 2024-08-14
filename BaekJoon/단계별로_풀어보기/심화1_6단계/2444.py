import sys
N = int(sys.stdin.readline().strip())
for i in range(1,N):
    print(' '*(N-i)+'*' * (2*i-1))
print('*' * (2*N-1))

for i in reversed(range(1,N)):
    print(' '*(N-i)+'*' * (2*i-1))