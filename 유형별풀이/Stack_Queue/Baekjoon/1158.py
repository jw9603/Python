# 1158 요세푸스 문제
# https://www.acmicpc.net/problem/1158

import sys

N, K = map(int,sys.stdin.readline().split())

a = [i for i in range(1,N+1)]

idx = 0

result = []

for _ in range(N):
    idx += K - 1
    
    if idx >= len(a):
        idx %= len(a)
        
    result.append(str(a.pop(idx)))

print('<'+', '.join(result)+'>')

    
