# 백준 2606. 바이러스
# https://www.acmicpc.net/problem/2606

########################## BFS 풀이 ##########################
import sys
from collections import defaultdict, deque
def bfs(graph, start):
    queue = deque([start])
    visited = [start]

    while queue:
        cur_v = queue.popleft()
        for next_v in graph[cur_v]:
            if next_v not in visited:
                visited.append(next_v)
                queue.append(next_v)
    return len(visited) - 1

def main():
    N = int(sys.stdin.readline().strip())
    M = int(sys.stdin.readline().strip())

    graph = defaultdict(list)

    for _ in range(M):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    print(bfs(graph, 1))

if __name__ == '__main__':
    main()
########################## BFS 풀이 ##########################
    
########################## DFS 풀이 ##########################
import sys
from collections import defaultdict

def dfs(graph, start, visited):
    visited.append(start)

    for next_v in graph[start]:
        if next_v not in visited:
            dfs(graph, next_v, visited)
    return visited

def main():
    N = int(sys.stdin.readline().strip())
    M = int(sys.stdin.readline().strip())

    graph = defaultdict(list)

    for _ in range(M):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    print(len(dfs(graph, 1, [])) - 1)

if __name__ == '__main__':
    main()
########################## DFS 풀이 ##########################