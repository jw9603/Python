# 백준 10026. 적록색약
# https://www.acmicpc.net/problem/10026
################################# 문제 이해 #################################
# 적록색약은 빨간색과 초록색의 차이를 거의 느끼지 못한다.
# 크기가 N x N인 그리드의 각 칸에 R, G, B 중 하나를 색칠한 그림이 있다.
# 그림은 몇 개의 구역으로 나뉘어져 있는데, 구역은 같은 색으로 이루어져 있다.
# 그림이 입력으로 주어졌을 때, 적록색약인 사람이 봤을 때와 아닌 사람이 봤을 때 구역의 수를 구해라.

# 입력
# 첫째 줄에 N이 주어집니다. 둘째 줄부터 N개의 줄에는 그림이 주어진다.
# 출력: 정상인 사람이 봤을 때의 구역의 개수와 적록색약인 사람이 봤을 때의 구역의 수를 출력


################################# 문제 이해 #################################
from collections import deque
def count_region(grid, N):
    visited = [[False] * N for _ in range(N)] 
    cnt = 0

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                cnt += 1
                bfs(i, j, grid[i][j], visited, grid, N)
    
    return cnt

def bfs(x, y, color, visited, grid, N):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([(x, y)])
    visited[x][y] = True

    while queue:
        cur_x, cur_y = queue.popleft()

        for dx, dy in directions:
            next_x, next_y = cur_x + dx, cur_y + dy

            if 0 <= next_x < N and 0 <= next_y < N:
                if not visited[next_x][next_y] and grid[next_x][next_y] == color:
                    visited[next_x][next_y] = True
                    queue.append((next_x, next_y))

def main():
    N = int(input().strip())
    grid = [list(input().strip()) for _ in range(N)]

    normal_cnt = count_region(grid, N)

    blind_grid = [['G' if grid[i][j] == 'R' else grid[i][j] for j in range(N)] for i in range(N)] 

    blind_cnt = count_region(blind_grid, N)

    print(normal_cnt, blind_cnt)

if __name__ == '__main__':
    main()