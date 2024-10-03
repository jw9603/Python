# 1436 - 영화감독 숌
# https://www.acmicpc.net/problem/1436

import sys

N = int(sys.stdin.readline().strip())

cnt = 0
res = 666

while True:
    
    if '666' in str(res):
        cnt += 1
    
    if cnt == N:
        break
    
    res += 1
    
print(res)