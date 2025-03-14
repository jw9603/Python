# 백준 2178. 미로 탐색
# https://www.acmicpc.net/problem/2178
import sys
from collections import deque
def bfs(N, M, graph):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = [[False] * M for _ in range(N)]
    queue = deque([(0, 0, 1)])

    while queue:
        cur_x, cur_y, cur_d = queue.popleft()
        if cur_x == N - 1 and cur_y == M - 1:
            return cur_d

        for dx, dy in directions:
            next_x, next_y = cur_x + dx, cur_y + dy
            if 0 <= next_x < N and 0 <= next_y < M:
                if graph[next_x][next_y] == 1 and not visited[next_x][next_y]:
                    visited[next_x][next_y] = True
                    queue.append((next_x, next_y, cur_d + 1))

def main():
    N, M = map(int, sys.stdin.readline().split())
    grid = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]

    print(bfs(N, M, grid))

if __name__ == '__main__':
    main()