# 백준 1707. 이분 그래프
# https://www.acmicpc.net/problem/1707
########################## BFS ##########################
import sys
from collections import deque, defaultdict
def bfs(graph, start, color):
    queue = deque([(start)])
    color[start] = 1

    while queue:
        cur_v = queue.popleft()

        for next_v in graph[cur_v]:
            if color[next_v] == 0:
                color[next_v] = -color[cur_v]
                queue.append(next_v)
            elif color[next_v] == color[cur_v]:
                return False
    return True

def check_bipartite(color, graph, vertex):

    for start in range(1, vertex + 1):
        if color[start] == 0:
            if not bfs(graph, start, color):
                return False
    return True

def main():
    K = int(sys.stdin.readline().strip())

    for _ in range(K):
        V, E = map(int, sys.stdin.readline().split())

        graph = defaultdict(list)

        for _ in range(E):
            u, v = map(int, sys.stdin.readline().split())
            graph[u].append(v)
            graph[v].append(u)
        
        color = [0] * (V + 1) # 0: 방문 안함, 1 or -1: 두 개의 그룹

        print("YES" if check_bipartite(color, graph, V) else "NO")
if __name__ == '__main__':
    main()
########################## BFS ##########################

########################## DFS ##########################
import sys
sys.setrecursionlimit(10 ** 6)
from collections import defaultdict
def dfs(graph, start, color, c):
    color[start] = c

    for next_v in graph[start]:
        if color[next_v] == 0:
            if not dfs(graph, next_v, color, -c):
                return False
        elif color[next_v] == color[start]:
            return False
    return True

def check_bipartite(color, graph, vertex):

    for start in range(1, vertex + 1):
        if color[start] == 0:
            if not dfs(graph, start, color, 1):
                return False
    return True

def main():
    K = int(sys.stdin.readline().strip())

    for _ in range(K):
        V, E = map(int, sys.stdin.readline().split())

        graph = defaultdict(list)

        for _ in range(E):
            u, v = map(int, sys.stdin.readline().split())
            graph[u].append(v)
            graph[v].append(u)
        
        color = [0] * (V + 1) # 0: 방문 안함, 1 or -1: 두 개의 그룹

        print("YES" if check_bipartite(color, graph, V) else "NO")
if __name__ == '__main__':
    main()
########################## DFS ##########################