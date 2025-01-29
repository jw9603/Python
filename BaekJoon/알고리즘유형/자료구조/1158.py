# 백준 1158. 요세푸스 문제
# https://www.acmicpc.net/problem/1158
import sys
from collections import deque
N, K = map(int, sys.stdin.readline().split())
def sol(N, K):
    q = deque()
    result = []
    for i in range(1, N + 1):
        q.append(i)
        
    while q:
        q.rotate(-(K - 1))
        result.append(q.popleft())
    
    return '<' + ', '.join(map(str, result)) + '>'
print(sol(N=N, K=K))
        
    