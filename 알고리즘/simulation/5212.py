# 백준 5212. 지구 온난화
# https://www.acmicpc.net/problem/5212
################################## 문제 이해 ##################################
# 상근이는 여행 떠남
# 지구 온난화로 인해 해수면이 상승해 섬의 일부가 바다에 잠겨버렸다.
# 다도해의 지도는 R x C 크기의 그리드로 나타낼 수 있다.
# 'X'는 땅, '.'는 바다를 나타낸다. 
# 50년이 지나면, 인접한 세 칸 또는 네 칸에 바다가 있는 땅은 모두 잠겨

# 입력
# R, C
# 출력: 50년 후의 지도를 출력

# 알고리즘
# 땅을 기준으로 상하좌우 그리드가 3개 이상 바다일 경우 해당 땅은 바다로 치환
# 그리고 바다가 되면 지도가 작아진다. 즉, 바다 부분은 출력 X
################################## 문제 이해 ##################################
def simulate(R, C, grid):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    future_grid = [['.'] * C for _ in range(R)]

    # 1. 50년 지난 후의 지도 그리기
    for x in range(R):
        for y in range(C):
            if grid[x][y] == 'X':
                sea = 0
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if not(0 <= nx < R and 0 <= ny < C) or grid[nx][ny] == '.':
                        sea += 1
                
                if sea < 3:
                    future_grid[x][y] = 'X'
    
    # 2. 새로운 지도 출력하기
    min_r, min_c = R, C
    max_r = max_c = -1
    
    for x in range(R):
        for y in range(C):
            if future_grid[x][y] == 'X':
                min_r = min(min_r, x)
                min_c = min(min_c, y)
                max_r = max(max_r, x)
                max_c = max(max_c, y)

    for i in range(min_r, max_r + 1):
        print(''.join(future_grid[i][min_c:max_c + 1]))

def main():
    R, C = map(int, input().split())
    grid = [list(input().strip()) for _ in range(R)]

    simulate(R, C, grid)

if __name__ == '__main__':
    main()