# 백준 2606. 바이러스
# https://www.acmicpc.net/problem/2606


########################## BFS 풀이 #############################
import sys
from collections import deque
from collections import defaultdict
n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())

def sol(n, m):
    graph = defaultdict(list)
    
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
        
    visited = [False] * (n + 1)
    queue = deque()
    queue.append(1)
    visited[1] = True
    cnt = 0
    
    while queue:
        cur_v = queue.popleft()
        for next_v in graph[cur_v]:
            if not visited[next_v]:
                visited[next_v] = True
                queue.append(next_v)
                cnt += 1
    return cnt
print(sol(n=n, m=m))
########################## BFS 풀이 #############################

########################## DFS 풀이 #############################
import sys
from collections import defaultdict
n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())

def sol(n, m):
    graph = defaultdict(list)
    
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
    visited = [False] * (n + 1)
    cnt = 0
    def dfs(node):
        nonlocal cnt
        visited[node] = True
        for next_node in graph[node]:
            if not visited[next_node]:
                cnt += 1
                dfs(next_node)
        
    dfs(1)
    print(cnt)
sol(n=n, m=m)
########################## DFS 풀이 #############################