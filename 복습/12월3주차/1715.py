# 백준 1715. 카드 정렬하기
# https://www.acmicpc.net/problem/1715
import sys
from heapq import heappush, heappop
N = int(sys.stdin.readline().strip())
def sol(N):
    heap = []
    for _ in range(N):
        heappush(heap, int(sys.stdin.readline().strip()))
    cnt = 0
    while len(heap) > 1:
        first = heappop(heap)
        second = heappop(heap)
        current_cnt = first + second
        cnt += current_cnt
        heappush(heap, current_cnt)
    print(cnt)
sol(N=N)
    