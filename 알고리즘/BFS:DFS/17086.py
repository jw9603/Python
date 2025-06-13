# 백준 17086. 아기 상어 2
# https://www.acmicpc.net/problem/17086
############################### 문제 이해 ###############################
# N * M 크기의 공간에 아기 상어 여러 마리가 있다. 한 칸에는 아기 상어 최대 1마리
# 어떤 칸의 안전 거리는 그 칸과 가장 거리가 가까운 아기 상어와의 거리이다.
# 두 칸의 거리는 하나의 칸에서 다른 칸으로 가기 위해서 지나야 하는 칸의 수, 이동은 8방향
# 안전 거리가 가장 큰 칸을 구해라.

# 입력
# N과 M

# 출력: 안전 거리의 최댓값

# 알고리즘
# 0은 빈 칸, 1은 아기 상어
# 1이 들어 있는 위치를 Queue에 넣어서, 안전 거리를 계속 업데이트 
############################### 문제 이해 ###############################
from collections import deque
def bfs(N, M, grid):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    queue = deque()
    visited = [[False] * M for _ in range(N)]
    max_dist = 0

    for i in range(N):
        for j in range(M):
            if grid[i][j] == 1:
                queue.append((i, j, 0))
                visited[i][j] = True

    while queue:
        cur_x, cur_y, cur_d = queue.popleft()

        for dx, dy in directions:
            next_x, next_y = cur_x + dx, cur_y + dy

            if 0 <= next_x < N and 0 <= next_y < M:
                if not visited[next_x][next_y]:
                    visited[next_x][next_y] = True
                    max_dist = max(max_dist, cur_d + 1)
                    queue.append((next_x, next_y, cur_d + 1))
    
    return max_dist

def main():
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]

    print(bfs(N, M, grid))

if __name__ == '__main__':
    main()