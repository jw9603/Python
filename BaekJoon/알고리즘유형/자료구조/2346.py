# 백준 2346. 풍선 터뜨리기
# https://www.acmicpc.net/problem/2346
import sys
from collections import deque
N = int(sys.stdin.readline().strip())
def sol(N):
    q = deque(enumerate(map(int, sys.stdin.readline().split())))
    result = []
    while len(q) >= 1:
        idx, paper = q.popleft()
        result.append(idx + 1)
        
        if paper > 0:
            q.rotate(-(paper - 1))
        else:
            q.rotate(-paper)
    return result
print(*sol(N=N))
