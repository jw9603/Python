# 백준 18352. 특정 거리의 도시 찾기
# https://www.acmicpc.net/problem/18352
################################ 문제 이해 ################################
# 1번부터 N번까지의 도시와 M개의 단방향 도로, 모든 도로의 거리는 1 -> 순수 BFS
# 이 때 특정한 도시 X로부터 출발하여 도달할 수 있는 모든 도시 중에서, 최단 거리가 정확히 K인
# 모든 도시들의 번호를 출력하는 프로그램.

# 1번부터 N번까지의 도시들이 있고, 특정 도시 X에서 출발하여 다른 도시들로 갈 때 최단 거리가
# K인 도시를 출력
################################ 문제 이해 ################################
from collections import defaultdict, deque
import sys
def bfs(N, graph, K, start, visited):
    queue = deque([start])
    visited[start] = 0

    while queue:
        cur_v = queue.popleft()

        for next_v in graph[cur_v]:
            if visited[next_v] == -1:
                visited[next_v] = visited[cur_v] + 1
                queue.append(next_v)
    
    result = [i for i in range(1, N + 1) if visited[i] == K]

    return result

def sol(N, K, X, graph):
    visited = [-1] * (N + 1)

    result = bfs(N, graph, K, X, visited)

    print(*sorted(result), end='\n') if result else print(-1)

def main():
    N, M, K, X = map(int, sys.stdin.readline().split())
    graph = defaultdict(list)

    for _ in range(M):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)

    sol(N, K, X, graph)

if __name__ == '__main__':
    main()
