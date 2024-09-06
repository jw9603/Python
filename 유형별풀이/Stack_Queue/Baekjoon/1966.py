# 1966번 - 프린터 큐
# https://www.acmicpc.net/problem/1966

# 중요도 점수가 높은것이 높은것임
import sys
from collections import deque
T = int(sys.stdin.readline().strip())

for _ in range(T):
    
    N, M = map(int,sys.stdin.readline().split())
    priority = list(map(int,sys.stdin.readline().split()))
    
    queue = deque((i,p) for i,p in enumerate(priority))
    
    print_order = 0
    
    while queue:
        
        current = queue.popleft()

        if any(current[1] < q[1] for q in queue):
            queue.append(current)
        else:
            print_order += 1
            if current[0] == M:
                print(print_order)
                break
