# 백준 7662. 이중 우선순위 큐
# https://www.acmicpc.net/problem/7662
import sys
from heapq import heappush, heappop
def sol(operations):
    min_heap = [] # 최솟값 삭제를 위한
    max_heap = [] # 쵀댓값 삭제를 위한
    entry_map = {}
    for operation in operations:
        num = int(operation[1])
        if operation[0] == 'I':
            heappush(min_heap, num)
            heappush(max_heap, -num)
            entry_map[num] = entry_map.get(num, 0) + 1
            
        elif operation[0] == 'D':
            if num == 1: # 최댓값 삭제
                while max_heap and entry_map.get(-max_heap[0], 0) == 0:
                    heappop(max_heap)
                
                if max_heap:
                    max_val = -heappop(max_heap)
                    entry_map[max_val] -= 1
    
            else:
                while min_heap and entry_map.get(min_heap[0], 0) == 0:
                    heappop(min_heap)
                if min_heap:
                    min_val = heappop(min_heap)
                    entry_map[min_val] -= 1

    while min_heap and entry_map.get(min_heap[0], 0) == 0:
        heappop(min_heap)
    while max_heap and entry_map.get(-max_heap[0], 0) == 0:
        heappop(max_heap)
    
    if not min_heap or not max_heap:
        return 'EMPTY'
    else:
        return f"{-max_heap[0]} {min_heap[0]}"
                
            
T = int(sys.stdin.readline().strip())
for _ in range(T):
    k = int(sys.stdin.readline().strip())
    operations = [sys.stdin.readline().split() for _ in range(k)]
    sol(operations=operations)