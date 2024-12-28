# 백준 1049. 기타줄
# https://www.acmicpc.net/problem/1049
import sys
from math import ceil
N, M = map(int, sys.stdin.readline().split())
prices = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
def sol(N, prices):
    min_package = float('inf')
    min_single = float('inf')
    for i, j in prices:
        min_package = min(i, min_package)
        min_single = min(j, min_single)
    
    cost_only_package = ceil(N / 6) * min_package
    cost_only_single = N * min_single
    cost_mix = (N // 6) * min_package + min(min_package, (N % 6) * min_single)
    return min(cost_only_package, cost_only_single, cost_mix)
print(sol(N=N, prices=prices))