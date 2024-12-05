# 14425. 문자열 집합
# https://www.acmicpc.net/problem/14425

import sys

N, M = map(int,sys.stdin.readline().split())
S = set()
for _ in range(N):
    S.add(sys.stdin.readline().strip())
    
def sol(S, M):
    result = 0
    for _ in range(M):
        if sys.stdin.readline().strip() in S:
            result += 1
    return result
print(sol(S=S, M=M))
