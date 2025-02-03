# 백준 3040. 백설 공주와 일곱 난쟁이
# https://www.acmicpc.net/problem/3040
import sys
from itertools import combinations
hats = [int(sys.stdin.readline().strip()) for _ in range(9)]

def sol(hats):
    total_sum = sum(hats)
    for comb in combinations(hats, 2):
        two_sum = sum(comb)
        if total_sum - two_sum == 100:
            return list(set(hats) - set(comb))

print(*sol(hats),sep='\n')
    