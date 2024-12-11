# 2485. 가로수
# https://www.acmicpc.net/problem/2485
import sys
from math import gcd
N = int(sys.stdin.readline().strip())
trees = [int(sys.stdin.readline().strip()) for _ in range(N)]

def sol(trees, N):
    distances = [trees[i + 1] - trees[i] for i in range(N-1)]

    interval = distances[0]
    for d in distances[1:]:
        interval = gcd(interval,d)

    total_trees = (trees[-1] - trees[0]) // interval + 1
    result = total_trees - N
    return result
print(sol(trees=trees, N=N))