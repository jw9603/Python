# 백준 1021. 회전하는 큐
# https://www.acmicpc.net/problem/1021
import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())
index = list(map(int, sys.stdin.readline().split()))

def sol(N, index):
    q = deque([i for i in range(1, N + 1)])
    cnt = 0
    
    for idx in index:
        while True:
            if q[0] == idx:
                q.popleft()
                break
            else:
                if q.index(idx) > len(q) // 2:
                    q.rotate(1)
                    cnt += 1
                else:
                    q.rotate(-1)
                    cnt += 1
    return cnt
print(sol(N=N, index=index))