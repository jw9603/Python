# 백준 1260. DFS와 BFS
# https://www.acmicpc.net/problem/1260
import sys
from collections import deque, defaultdict
def dfs(graph, start_v, visited):
    visited.append(start_v)
    for next_v in sorted(graph[start_v]):
        if next_v not in visited:
            dfs(graph, next_v, visited)
    return visited

def bfs(graph, start_v):
    visited = [start_v]
    q = deque()
    q.append(start_v)
    while q:
        cur_v = q.popleft()
        for next_v in sorted(graph[cur_v]):
            if next_v not in visited:
                visited.append(next_v)
                q.append(next_v)
    return visited
def main():
    N, M, V = map(int, sys.stdin.readline().split())
    graph = defaultdict(list)
    for _ in range(M):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
    
    dfs_result = dfs(graph, V, [])
    bfs_result = bfs(graph, V)
    print(*dfs_result)
    print(*bfs_result)

main()