# 백준 17144. 미세먼지 안녕!
# https://www.acmicpc.net/problem/17144
################################ 문제 이해 ################################
# 1초 동안 아래 일이 순서대로 일어난다.
# 1. 미세먼지가 확산된다. 확산은 메시먼지가 있는 모든 칸에서 동시에 발생
    # 1.1 (r, c)에 있는 미세먼지는 인접한 네 방향으로 확산
    # 1.2 인접한 방향에 공기청정기가 있거나, 칸이 없으면 그 방향으로 확산이 일어나지 않는다.
    # 1.3 확산되는 양은 A_{r, c} // 5
    # 1.4 (r, c)에 남은 미세먼지의 양은 A_{r, c} - [A_{r, c} // 5] * (확산 방향의 개수)

# 2. 공기청정기 작동
    # 2.1 위쪽 공기청기의 바람은 반시계방향으로 순환, 아래쪽 공기청정기는 시계방향으로 순환
    # 2.2 바람이 불면 미세먼지가 바람의 방향대로 모두 한 칸씩 이동
def spread_dust(grid, R, C):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    tmp = [[0] * C for _ in range(R)]

    for r in range(R):
        for c in range(C):
            if grid[r][c] > 0:
                spread_amount = grid[r][c] // 5
                dir_cnt = 0

                # 1.1 (r, c)에 있는 미세먼지는 인접한 네 방향으로 확산
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    # 1.2 인접한 방향에 공기청정기가 있거나, 칸이 없으면 그 방향으로 확산이 일어나지 않는다.
                    if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] != -1:
                        # 1.3 확산되는 양은 A_{r, c} // 5
                        tmp[nr][nc] += spread_amount
                        dir_cnt += 1
                        
                # 1.4 (r, c)에 남은 미세먼지의 양은 A_{r, c} - [A_{r, c} // 5] * (확산 방향의 개수)
                grid[r][c] -= spread_amount * dir_cnt
    
    # 1.5 확산하기전의 위치의 확산후의 계산은 완료했으니, 확산된 곳의 값을 계산해야 함.
    for r in range(R):
        for c in range(C):
            grid[r][c] += tmp[r][c]

def operate_air_cleaner(grid, cleaner, R, C):
    directions1 = [(0, 1), (-1, 0), (0, -1), (1, 0)] # 반시계
    directions2 = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 시계

    # 위쪽 - 반시계
    x, y = cleaner[0], 0
    d = 0
    tmp = 0

    while True:
        # 2.2 바람이 불면 미세먼지가 바람의 방향대로 모두 한 칸씩 이동
        nx, ny = x + directions1[d][0], y + directions1[d][1]

        if 0 <= nx < R and 0 <= ny < C:
            if grid[nx][ny] != -1:
                grid[nx][ny], tmp = tmp, grid[nx][ny]
                x, y = nx, ny
            else:
                break
        else:
            d += 1
    
    # 아래쪽 - 시계
    x, y = cleaner[1], 0
    d = 0
    tmp = 0

    while True:
        nx, ny = x + directions2[d][0], y + directions2[d][1]

        if 0 <= nx < R and 0 <= ny < C:
            if grid[nx][ny] != -1:
                grid[nx][ny], tmp = tmp, grid[nx][ny]
                x, y = nx, ny
            else:
                break
        else:
            d += 1

def simulate(R, C, T, grid, cleaner):
    result = 0

    for _ in range(T):
        # 1. 미세먼지가 확산된다.
        spread_dust(grid, R, C)
        # 2. 공기청정기 작동
        operate_air_cleaner(grid, cleaner, R, C)
    
    # 3. T초가 지난 후 남아있는 미세먼지의 양 반환
    for i in range(R):
        for j in range(C):
            if grid[i][j] > 0:
                result += grid[i][j]
    
    return result
    
def main():
    R, C, T = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(R)]

    cleaner = []
    for i in range(R):
        if grid[i][0] == -1:
            cleaner.append(i)
        
    print(simulate(R, C, T, grid, cleaner))

if __name__ == '__main__':
    main()