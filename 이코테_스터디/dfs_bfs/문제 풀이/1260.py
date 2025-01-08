# 백준 1260. DFS와 BFS
# https://www.acmicpc.net/problem/1260
import sys
from collections import deque, defaultdict

def bfs(graph, start_v):
    queue = deque()
    queue.append(start_v)
    visited = [start_v]
    while queue:
        cur_v = queue.popleft()
        for next_v in sorted(graph[cur_v]):
            if next_v not in visited:
                visited.append(next_v)
                queue.append(next_v)
    return visited
    
        
    
    

def dfs(graph, start_v, visited):
    visited.append(start_v)
    
    for next_v in sorted(graph[start_v]):
        if next_v not in visited:
            dfs(graph, next_v, visited)
    return visited

def sol():
    n, m, v = map(int, sys.stdin.readline().split())
    graph = defaultdict(list)
    
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
    
    # BFS 실행
    bfs_result = bfs(graph=graph, start_v=v)
    
    # DFS 실행
    dfs_result = dfs(graph=graph, start_v=v, visited= [])
    print(*dfs_result)
    print(*bfs_result)
sol()