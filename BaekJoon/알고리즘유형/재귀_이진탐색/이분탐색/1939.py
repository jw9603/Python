# 백준 1939. 중량제한
# https://www.acmicpc.net/problem/1939
import sys
from collections import deque, defaultdict
N, M = map(int, sys.stdin.readline().split())
bridges = [tuple(map(int, sys.stdin.readline().split())) for _ in range(M)]
start, end = map(int, sys.stdin.readline().split())
def bfs(graph, start, end, weight, visited):
    queue = deque()
    queue.append(start)
    visited[start] = True
    
    while queue:
        cur_v = queue.popleft()
        if cur_v == end:
            return True
        for next_v, limit in graph[cur_v]:
            if not visited[next_v] and limit >= weight:
                visited[next_v] = True
                queue.append(next_v)
    return False

def sol(N, M, bridges, start, end):
    
    graph = defaultdict(list)
    max_weight = 0
    for a, b, c in bridges:
        graph[a].append((b, c))
        graph[b].append((a, c))
        max_weight = max(max_weight, c)
    
    left, right = 1, max_weight
    result = 0
    
    while left <= right:
        mid = (left + right) // 2
        visited = [False] * (N + 1)
        
        if bfs(graph, start, end, mid, visited):
            result = mid
            left = mid + 1
        else:
            right = mid - 1
    return result
print(sol(N=N, M=M, bridges=bridges, start=start, end=end))