# 백준 11724. 연결 요소의 개수
# https://www.acmicpc.net/problem/11724
##################################### 문제 이해 #####################################
# 방향없는 그래프가 주어졌을 때, 연결 요소의 개수를 구해라
# 입력:
# 첫째 줄에 정점의 개수 N와 간선의 개수 M가 주어짐.
# 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다.

# 알고리즘
# 연결되어 있는 요소를 찾으면 되기 때문에, 모든 정점에서 시작하여 연결이 끝날때까지 순회를 하면 된다.
# 순회는? BFS, DFS!!

##################################### 문제 이해 #####################################
# 1. BFS
from collections import deque, defaultdict
import sys
def bfs(start, graph, visited):
    visited[start] = True
    q = deque([start])

    while q:
        cur_v = q.popleft()
        for next_v in graph[cur_v]:
            if not visited[next_v]:
                visited[next_v] = True
                q.append(next_v)

def sol(graph, N):
    visited = [False] * (N + 1)
    cnt = 0

    for i in range(1, N + 1):
        if not visited[i]:
            bfs(i, graph, visited)
            cnt += 1
    
    return cnt

def main():
    N, M = map(int, sys.stdin.readline().split())
    graph = defaultdict(list)
    for _ in range(M):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)
    
    print(sol(graph, N))

if __name__ == '__main__':
    main()

# 2. DFS
from collections import defaultdict
import sys
sys.setrecursionlimit(10 ** 6)
def dfs(start, graph, visited):
    visited[start] = True

    for next_v in graph[start]:
        if not visited[next_v]:
            dfs(next_v, graph, visited)

def sol(graph, N):
    visited = [False] * (N + 1)
    cnt = 0

    for i in range(1, N + 1):
        if not visited[i]:
            dfs(i, graph, visited)
            cnt += 1
    
    return cnt
def main():
    N, M = map(int, sys.stdin.readline().split())
    graph = defaultdict(list)
    for _ in range(M):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)
    
    print(sol(graph, N))

if __name__ == '__main__':
    main()