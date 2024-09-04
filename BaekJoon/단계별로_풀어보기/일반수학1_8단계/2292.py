# 2292 벌집
# https://www.acmicpc.net/problem/2292

import sys

N = int(sys.stdin.readline().strip())

step = 1
cnt = 1

while cnt < N:
    cnt += 6 * step
    step += 1
    
print(step)