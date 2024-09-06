# 2501 약수구하기
# https://www.acmicpc.net/problem/2501

import sys

N, K = map(int,sys.stdin.readline().split())
num = []
for k in range(1,N+1):
    
    if N % k == 0:
        num.append(k)
        
print(num[K-1] if K <= len(num) else 0)
        
