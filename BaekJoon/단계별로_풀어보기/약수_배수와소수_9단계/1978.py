# 1978 - 소수 찾기
# https://www.acmicpc.net/problem/1978

import sys

N = int(sys.stdin.readline().strip())

nums = list(map(int,sys.stdin.readline().split()))

sosu = 0
for num in nums:
    cnt = 0
    if num == 1: # 1은 소수가 아니야.
        continue
    for i in range(2,num+1):
        if num % i == 0:
            cnt += 1

    if cnt == 1:
        sosu += 1

print(sosu)
            
