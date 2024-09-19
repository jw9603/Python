# 분해합 - 2231
# https://www.acmicpc.net/problem/2231

# M의 분해합이 N인 경우, M을 N의 생성자라 한다.


import sys

N = int(sys.stdin.readline().strip())
res = 0
for i in range(1,N+1):
    
    nums = list(map(int,str(i)))
    res = sum(nums) + i
    
    if res == N:
        print(i)
        break
    
    if i == N:
        print(0)