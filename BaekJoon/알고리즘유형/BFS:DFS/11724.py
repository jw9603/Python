# 백준 11724. 연결 요소의 개수
# https://www.acmicpc.net/problem/11724
################################## BFS 풀이 #############################
import sys
from collections import defaultdict, deque

def bfs(node, graph, visited):
    visited[node] = True
    q = deque([node])
    
    while q:
        cur_v = q.popleft()
        for next_v in graph[cur_v]:
            if not visited[next_v]:
                visited[next_v] = True
                q.append(next_v)
                

def count_connected_component(N, graph):
    visited = [False] * (N + 1)
    cnt = 0
    
    for vertex in range(1, N + 1):
        if not visited[vertex]:
            bfs(vertex, graph, visited)
            cnt += 1
    return cnt

def main():
    N, M = map(int, sys.stdin.readline().split())
    graph = defaultdict(list)
    for _ in range(M):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)
    print(count_connected_component(N=N, graph=graph))
main()
################################## BFS 풀이 #############################

################################## DFS 풀이 #############################
import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)
def dfs(node, graph, visited):
    visited[node] = True
    for next_v in graph[node]:
        if not visited[next_v]:
            dfs(next_v, graph, visited)

def count_connected_component(N, graph):
    visited = [False] * (N + 1)
    cnt = 0
    for vertex in range(1, N + 1):
        if not visited[vertex]:
            dfs(vertex, graph, visited)
            cnt += 1
    return cnt

def main():
    N, M = map(int, sys.stdin.readline().split())
    graph = defaultdict(list)
    for _ in range(M):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)
    print(count_connected_component(N=N, graph=graph))
main()
################################## DFS 풀이 #############################