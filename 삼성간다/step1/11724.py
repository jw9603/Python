# 백준 11724. 연결 요소의 개수
# https://www.acmicpc.net/problem/11724
##################################### BFS #####################################
import sys
from collections import defaultdict, deque
def bfs(start, visited, graph):
    visited[start] = True
    queue = deque([start])

    while queue:
        cur_v = queue.popleft()

        for next_v in graph[cur_v]:
            if not visited[next_v]:
                visited[next_v] = True
                queue.append(next_v)

def count_connected_component(N, graph):
    visited = [False] * (N + 1)
    cnt = 0
    for vertex in range(1, N + 1):
        if not visited[vertex]:
            bfs(vertex, visited, graph)
            cnt += 1
    return cnt
def main():
    N, M = map(int, sys.stdin.readline().split())
    graph = defaultdict(list)
    for _ in range(M):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)
    print(count_connected_component(N, graph))

if __name__ == '__main__':
    main()
##################################### BFS #####################################

##################################### DFS #####################################
import sys
from collections import defaultdict
sys.setrecursionlimit(10 ** 6)
def dfs(start, visited, graph):
    visited[start] = True
    
    for next_v in graph[start]:
        if not visited[next_v]:
            dfs(next_v, visited, graph)

def count_connected_component(N, graph):
    visited = [False] * (N + 1)
    cnt = 0
    for vertex in range(1, N + 1):
        if not visited[vertex]:
            dfs(vertex, visited, graph)
            cnt += 1
    return cnt
def main():
    N, M = map(int, sys.stdin.readline().split())
    graph = defaultdict(list)
    for _ in range(M):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)
    print(count_connected_component(N, graph))

if __name__ == '__main__':
    main()
##################################### DFS #####################################