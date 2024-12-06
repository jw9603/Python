# 1764. 듣보잡
# https://www.acmicpc.net/problem/1764

import sys

N, M = map(int,sys.stdin.readline().split())
listen = set()
see = set()

for _ in range(N):
    listen.add(sys.stdin.readline().strip())
for _ in range(M):
    see.add(sys.stdin.readline().strip())

def sol(listen, see):
    a = sorted(listen & see)
    return len(a),'\n'.join(i for i in a)

a, b = sol(listen=listen, see=see)
print(a, b, sep='\n')

