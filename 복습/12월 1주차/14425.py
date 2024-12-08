# 14425. 문자열 집합
# https://www.acmicpc.net/problem/14425

import sys
N, M = map(int,sys.stdin.readline().split())
set_n = set()

for _ in range(N):
    set_n.add(sys.stdin.readline().strip())
result = 0
for _ in range(M):
    if sys.stdin.readline().strip() in set_n:
        result += 1
    
print(result)