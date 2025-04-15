# 백준 2667. 단지번호붙이기
# https://www.acmicpc.net/problem/2667

# 1은 집이 있는 곳, 0은 집이 없는 곳
# 상하좌우
# 총 단지수, 각 단지에 속하는 집의 수
############################ BFS ############################
from collections import deque
def bfs(x, y, N, grid, visited):
    visited[x][y] = True
    queue = deque([(x, y)])
    cnt = 1
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        cur_x, cur_y = queue.popleft()

        for dx, dy in directions:
            next_x, next_y = cur_x + dx, cur_y + dy

            if 0 <= next_x < N and 0 <= next_y < N:
                if grid[next_x][next_y] == 1 and not visited[next_x][next_y]:
                    visited[next_x][next_y] = True
                    queue.append((next_x, next_y))
                    cnt += 1
    return cnt

def solution(N, grid):
    visited = [[False] * N for _ in range(N)]
    home_cnt = 0
    home_info = []
    
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 1 and not visited[i][j]:
                home_info.append(bfs(i, j, N, grid, visited))
                home_cnt += 1
    
    print(home_cnt)
    print(*sorted(home_info), sep='\n')

def main():
    N = int(input().strip())
    grid = [list(map(int, input().strip())) for _ in range(N)]

    solution(N, grid)

if __name__ == '__main__':
    main()
############################ BFS ############################

############################ BFS ############################
def dfs(x, y, N, grid, visited):
    visited[x][y] = True
    cnt = 1
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dx, dy in directions:
        next_x, next_y = x + dx, y + dy

        if 0 <= next_x < N and 0 <= next_y < N:
            if grid[next_x][next_y] == 1 and not visited[next_x][next_y]:
                cnt += dfs(next_x, next_y, N, grid, visited)
    
    return cnt


def solution(N, grid):
    visited = [[False] * N for _ in range(N)]
    home_cnt = 0
    home_info = []
    
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 1 and not visited[i][j]:
                home_info.append(dfs(i, j, N, grid, visited))
                home_cnt += 1
    
    print(home_cnt)
    print(*sorted(home_info), sep='\n')

def main():
    N = int(input().strip())
    grid = [list(map(int, input().strip())) for _ in range(N)]

    solution(N, grid)

if __name__ == '__main__':
    main()
############################ BFS ############################