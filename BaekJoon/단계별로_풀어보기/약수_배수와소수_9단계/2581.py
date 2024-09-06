# 2581 - 소수
# https://www.acmicpc.net/problem/2581

import sys

M = int(sys.stdin.readline().strip())
N = int(sys.stdin.readline().strip())

sosu = []

for i in range(M,N+1):
    cnt = 0
    for j in range(2,i+1):
        if i % j == 0:
            cnt += 1
        
    if cnt == 1:
        sosu.append(i)
        
if len(sosu):
    print(sum(sosu))
    print(sosu[0])
else:
    print(-1)
        