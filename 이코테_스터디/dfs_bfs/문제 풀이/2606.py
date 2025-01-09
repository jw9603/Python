# 백준 2606. 바이러스
# https://www.acmicpc.net/problem/2606

####################### BFS 풀이 ###########################
from collections import deque, defaultdict
import sys

n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())
graph = defaultdict(list)
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def sol(graph, start_v):
    visited = [start_v]
    queue = deque()
    queue.append(start_v)
    
    while queue:
        cur_v = queue.popleft()
        for next_v in graph[cur_v]:
            if next_v not in visited:
                visited.append(next_v)
                queue.append(next_v)
    return len(visited) - 1
print(sol(graph=graph, start_v=1))
####################### BFS 풀이 ###########################

####################### DFS 풀이 ###########################
from collections import defaultdict
import sys
n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())
graph = defaultdict(list)
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
    
def sol(graph, start_v, visited):
    visited.append(start_v)
    
    for next_v in graph[start_v]:
        if next_v not in visited:
            sol(graph, next_v, visited)
    return len(visited) - 1
print(sol(graph=graph, start_v=1, visited=[]))
####################### DFS 풀이 ###########################
