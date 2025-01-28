# 백준 2164. 카드2
# https://www.acmicpc.net/problem/2164
import sys
from collections import deque
N = int(sys.stdin.readline().strip())

def sol(N):
    queue = deque()
    for i in range(1, N + 1):
        queue.append(i)
        
    while len(queue) > 1:
        queue.popleft()
        queue.append(queue.popleft())
    print(*queue)
sol(N=N)
    
    