# 백준 1202. 보석 도둑
# https://www.acmicpc.net/problem/1202
import sys
from heapq import heappush, heappop
N, K = map(int, sys.stdin.readline().split())
jewels = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
bags = [int(sys.stdin.readline().strip()) for _ in range(K)]

def sol(N, jewels, bags):
    jewels.sort()
    bags.sort()
    max_price = 0
    idx = 0
    heap = []
    for bag in bags:
        while idx < N and jewels[idx][0] <= bag:
            heappush(heap, -(jewels[idx][1]))
        if heap:
            max_price -= heappop(heap)
    print(max_price)
sol(N=N, jewels=jewels, bags=bags)
            