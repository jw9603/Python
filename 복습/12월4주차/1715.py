# 백준 1715. 카드 정렬하기
# https://www.acmicpc.net/problem/1715
import sys
from heapq import heappop, heappush
N = int(sys.stdin.readline().strip())
def sol(N):
    result = 0
    heap = []
    for _ in range(N):
        heappush(heap, int(sys.stdin.readline().strip()))
    
    while len(heap) > 1:
        first = heappop(heap)
        second = heappop(heap)
        
        current_result = first + second
        result += current_result
        heappush(heap, current_result)
    return result
print(sol(N=N))