# 백준 2161. 카드1
# https://www.acmicpc.net/problem/2161
import sys
from collections import deque
N = int(sys.stdin.readline().strip())
def sol(N):
    q = deque([i for i in range(1, N + 1)])
    throw = []
    while len(q) > 1:
        throw.append(q.popleft())
        q.append(q.popleft())
    
    return throw + list(q)
print(*sol(N=N))