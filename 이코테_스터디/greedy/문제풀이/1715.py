# 1715. 카드 정렬하기
# https://www.acmicpc.net/problem/1715
import sys
from heapq import heappush, heappop

N = int(sys.stdin.readline().strip())

def sol(N):
    heap = []
    result = 0
    for _ in range(N):
        heappush(heap, int(sys.stdin.readline().strip()))
    
    while len(heap) > 1:
        first = heappop(heap)
        second = heappop(heap)
        
        current_cost = first + second
        result += current_cost
        heappush(heap, current_cost)
    return result
print(sol(N=N))