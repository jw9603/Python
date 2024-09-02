import sys

T = int(sys.stdin.readline().strip())

for _ in range(T):
    R, S = sys.stdin.readline().split()
    print(''.join([S[i]*int(R) for i in range(len(S))]))