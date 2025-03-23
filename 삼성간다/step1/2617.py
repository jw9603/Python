# 백준 2617. 구슬 찾기
# https://www.acmicpc.net/problem/2617
############################## BFS ##############################
import sys
from collections import defaultdict, deque
def bfs(start, graph, N):
    queue = deque([start])
    visited = [False] * (N + 1)
    visited[start] = True
    cnt = 0

    while queue:
        cur_v = queue.popleft()

        for next_v in graph[cur_v]:
            if not visited[next_v]:
                visited[next_v] = True
                queue.append(next_v)
                cnt += 1
    return cnt

def main():
    N, M = map(int, sys.stdin.readline().split())
    heavier, lighter = defaultdict(list), defaultdict(list)

    for _ in range(M):
        heavy, light = map(int, sys.stdin.readline().split())
        heavier[light].append(heavy)
        lighter[heavy].append(light)
    
    mid = (N + 1) // 2
    not_possible = 0

    for i in range(1, N + 1):
        heavy_cnt = bfs(i, heavier, N)
        light_cnt = bfs(i, lighter, N)

        if heavy_cnt >= mid or light_cnt >= mid:
            not_possible += 1
    print(not_possible)

if __name__ == '__main__':
    main()
############################## BFS ##############################

############################## DFS ##############################
import sys
from collections import defaultdict
def dfs(start, graph, visited):

    visited[start] = True
    cnt = 1

    for next_v in graph[start]:
        if not visited[next_v]:
            cnt += dfs(next_v, graph, visited)
          
    return cnt

def main():
    N, M = map(int, sys.stdin.readline().split())
    heavier, lighter = defaultdict(list), defaultdict(list)

    for _ in range(M):
        heavy, light = map(int, sys.stdin.readline().split())
        heavier[light].append(heavy)
        lighter[heavy].append(light)
    
    mid = (N + 1) // 2
    not_possible = 0

    for i in range(1, N + 1):
        visited = [False] * (N + 1)
        heavy_cnt = dfs(i, heavier, visited) - 1
        light_cnt = dfs(i, lighter, visited) - 1

        if heavy_cnt >= mid or light_cnt >= mid:
            not_possible += 1
    print(not_possible)

if __name__ == '__main__':
    main()
############################## DFS ##############################