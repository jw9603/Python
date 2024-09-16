# 2217 - 로프
# https://www.acmicpc.net/problem/2217

import sys

def sol(N,lope):
    ans = []
    lope.sort()
    for i in lope:
        ans.append(i * N)
        N -= 1
    return max(ans)


N = int(sys.stdin.readline().strip())
lope = []
for _ in range(N):
    lope.append(int(sys.stdin.readline().strip()))

print(sol(N,lope))
    