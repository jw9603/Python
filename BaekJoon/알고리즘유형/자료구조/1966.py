# 백준 1966. 프린터 큐
# https://www.acmicpc.net/problem/1966
import sys
from collections import deque

def sol(priority):
    queue = deque((i, p) for i, p in enumerate(priority))
    
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
    
T = int(sys.stdin.readline().strip())
for _ in range(T):
    # N: 문서의 개수, M: 몇 번째로 인쇄되었는지 궁금한 문서가 현재 Queue에서 몇 번째에 놓여 있는지를 나타내는 정수
    N, M = map(int, sys.stdin.readline().split())
    priority = list(map(int, sys.stdin.readline().split()))
    
    sol(priority=priority)
            