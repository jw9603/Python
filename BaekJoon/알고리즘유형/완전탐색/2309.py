# 백준 2309. 일곱 난쟁이
# https://www.acmicpc.net/problem/2309
import sys
from itertools import combinations
heights = [int(sys.stdin.readline().strip()) for _ in range(9)]
def sol(heights):
    total_height = sum(heights)
    for comb in combinations(heights, 2):
        if total_height - sum(comb) == 100:
            return sorted(list(set(heights) - set(comb)))
print(*sol(heights=heights),sep='\n')