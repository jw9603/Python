# 백준 11000. 강의실 배정
# https://www.acmicpc.net/problem/11000
import sys
from heapq import heappush, heappop
N = int(sys.stdin.readline().strip())
classes = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
def sol(classes):
    classes.sort()
    heap = []
    for start, end in classes:
        if heap and heap[0] <= start:
            heappop(heap)
        heappush(heap, end)
    return len(heap)
print(sol(classes=classes))