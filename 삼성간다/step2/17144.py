# 백준 17144. 미세먼지 안녕!
# https://www.acmicpc.net/problem/17144

# 공기청정기는 항상 1번 열에 설치되어 있고, 크기는 두 행을 차지한다.
# 공기청정기가 설치되어 있지 않은 칸에는 미세먼제가 있고, (r, c)에 있는 미세먼지의 양은 A_r, c이다.

# 1초 동안 아래 적힌 일이 순서대로 일어남

# 1. 미세먼지가 확산된다. 확산은 미세먼지가 있는 모든 칸에서 동시에 일어남
# 인접한 네방향(상, 하, 좌, 우) -> 방향 check
    # 인접한 방향에 공기청정기가 있거나, 칸이 없으면 일어나지 않음 -> 조건!!
    # 확산 되는 양은 A_{r, c} // 5
    # (r, c)에 남아 있는 미세 먼지의 양은 A_{r, c} - [A_{r, c} // 5] * 확산된 방향의 개수
def spread_dust(R, C, grid):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    tmp = [[0] * C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if grid[r][c] > 0:
                spread_amount = grid[r][c] // 5
                cnt = 0
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] != -1:
                        tmp[nr][nc] += spread_amount
                        cnt += 1
                grid[r][c] -= spread_amount * cnt
    
    for r in range(R):
        for c in range(C):
            grid[r][c] += tmp[r][c]

# 2. 공기청정기가 작동
# 바람이 나온다.
# 위쪽은 반시계로 순환, 아래쪽은 시계방향으로 순환
# 바람이 불면 미세먼지가 바람의 방향대로 1칸씩 이동
def operate_air_cleaner(R, C, grid, cleaner):

    direction1 = [(0, 1), (-1, 0), (0, -1), (1, 0)] # 반시계 방향
    direction2 = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 시계 방향

    # 위쪽 - 반시계
    x, y = cleaner[0], 0
    i = 0
    tmp = 0
    while True:
        nx, ny = x + direction1[i][0], y + direction2[i][1]

        if 0 <= nx < R and 0 <= ny < C:
            if grid[nx][ny] != -1:
                grid[nx][ny], tmp = tmp, grid[nx][ny]

                x, y = nx, ny
            else:
                break
        else:
            i += 1

    # 아래쪽 - 시계
    i = 0
    x, y = cleaner[1], 0
    tmp = 0
    while True:
        nx, ny = x + direction2[i][0], y + direction2[i][1]
        
        if 0 <= nx < R and 0 <= ny < C:
            if grid[nx][ny] != -1:
                grid[nx][ny], tmp = tmp, grid[nx][ny]
                x, y = nx, ny
            else:
                break
        else:
            i += 1

def simulate(R, C, T, grid, cleaner):
    
    for _ in range(T):
        spread_dust(R, C, grid)
        operate_air_cleaner(R, C, grid, cleaner)
    
    total = 0

    for r in range(R):
        for c in range(C):
            if grid[r][c] > 0:
                total += grid[r][c]
    return total

def main():
    R, C, T = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(R)]

    cleaner = []
    for i in range(R):
        if grid[i][0] == -1:
            cleaner.append(i)
    
    result = simulate(R, C, T, grid, cleaner)
    print(result)

if __name__ == '__main__':
    main()