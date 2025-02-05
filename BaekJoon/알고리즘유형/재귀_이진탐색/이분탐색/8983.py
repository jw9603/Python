# 백준 8983. 사냥꾼
# https://www.acmicpc.net/problem/8983
import sys
from bisect import *
M, N, L = map(int, sys.stdin.readline().split())
shootings = list(map(int, sys.stdin.readline().split()))
animals = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]

def sol(M, L, shootings, animals):
    shootings.sort()
    cnt = 0
    for x, y in animals:
        idx = bisect_left(shootings, x)
        
        if 0 <= idx < M:
            if abs(shootings[idx] - x) + y <= L:
                cnt += 1
                continue
        for i in [idx, idx - 1]:
            if 0 <= i < M:
                if abs(shootings[i] - x) + y <= L:
                    cnt += 1
                    break
    return cnt
print(sol(M=M, L=L, shootings=shootings, animals=animals))
