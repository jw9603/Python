# 백준 1967. 트리의 지름
# https://www.acmicpc.net/problem/1967
import sys
from collections import defaultdict
sys.setrecursionlimit(10 ** 6)

n = int(sys.stdin.readline().strip())
graph = defaultdict(list)
for _ in range(n - 1):
    parent, child, weight = map(int, sys.stdin.readline().split())
    graph[parent].append((child, weight))
    graph[child].append((parent, weight))
    

visited = [False] * (n + 1)
max_distance = 0
farthest_node_from_root = 0
def dfs(node, distance):
    
    global max_distance, farthest_node_from_root
    visited[node] = True
    
    if distance > max_distance:
        max_distance = distance
        farthest_node_from_root = node
    
    for next_node, weight in graph[node]:
        if not visited[next_node]:
            dfs(next_node, distance + weight)

dfs(1, 0)

visited = [False] * (n + 1)
max_distance = 0
dfs(farthest_node_from_root, 0)
print(max_distance)
    