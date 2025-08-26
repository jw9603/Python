# 백준 14940. 쉬운 최단거리
# https://www.acmicpc.net/problem/14940
############################## 문제 이해 ##############################
# 지도가 주어지면 모든 지점에 대해서 목표지점까지의 거리를 구하여라.
# 가로와 세로로만 움직일 수 있다.

# 입력:
# 지도의 크기 n과 m이 주어진다. n은 세로, m은 가로.
# 0은 갈 수 없는 땅, 1은 갈 수 있는 땅, 2는 목표 지점이다.
############################## 문제 이해 ##############################
from collections import deque
def bfs(graph, dist, start, n, m):
    sx, sy = start
    queue = deque([(sx, sy)])
    dist[sx][sy] = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        x, y = queue.popleft()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1 and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    queue.append((nx, ny))
    
    return dist

def sol(graph, n, m):
    dist = [[-1] * m for _ in range(n)]
    target = None

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2:
                target = (i, j)
            if graph[i][j] == 0:
                dist[i][j] = 0
    
    bfs(graph, dist, target, n, m)

    for row in dist:
        print(*row)

def main():
    n, m = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]

    sol(graph, n, m)

if __name__ == "__main__":
    main()