# 백준 18352. 특정 거리의 도시 찾기
# https://www.acmicpc.net/problem/18352
import sys
from collections import deque, defaultdict
def bfs(N, K, start, graph, visited):
    queue = deque([start])
    visited[start] = 0

    while queue:
        cur_v = queue.popleft()

        for next_v in graph[cur_v]:
            if visited[next_v] == -1:
                visited[next_v] = visited[cur_v] + 1
                queue.append(next_v)
    result = [i for i in range(1, N + 1) if visited[i] == K]

    print(*result, sep='\n') if result else print(-1)

def main():
    N, M, K, X = map(int, sys.stdin.readline().split())
    graph = defaultdict(list)
    for _ in range(M):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
    
    visited = [-1] * (N + 1)

    bfs(N, K, X, graph, visited)

if __name__ == '__main__':
    main()