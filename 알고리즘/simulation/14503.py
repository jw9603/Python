# 백준 14503. 로봇 청소기
# https://www.acmicpc.net/problem/14503
##################################### 문제 이해 #####################################
# 로봇 청소기와 방의 상태가 주어졌을 때, 청소하는 영역의 개수를 구하는 프로그램을 작성해라.
# 방: N x M 크기의 직사각형
# 각각의 칸은 벽 또는 빈 칸이다.
# 청소기는 바라보는 방향이 있으며, 동서남북중 하나
# 처음에 빈 칸은 전부 청소되지 않은 상태

# 1. 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
# 2. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우,
    # 2-1. 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
    # 2-2. 바라보는 방향의 뒤쪽칸이 벽이라 후진할 수 없다면 멈춘다.
# 3. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우,
    # 3-1. 반시계 방향으로 90도 회전
    # 3-2. 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진
    # 3-3. 1번으로 돌아간다. (현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.)
##################################### 문제 이해 #####################################
def simulate(grid, N, M, r, c, d):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 북, 동, 남, 서
    visited = [[False] * M for _ in range(N)]
    visited[r][c] = True
    cnt = 1

    while True:
        found = False

        # 처음에는 모두다 청소가 되어있지 않다, 방의 가장자리를 제외하곤,,,
        # 하지만 시작 점에서 4방향중 하나 이상은 무조건 청소 안된곳
        # 그러므로 아래 코드를 가장 먼저 실행해야 함.
        # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우,
        for _ in range(4):
            d =  (d - 1) % 4
            next_r, next_c = r + directions[d][0], c + directions[d][1]
            if 0 <= next_r < N and 0 <= next_c < M:
                if grid[next_r][next_c] == 0 and not visited[next_r][next_c]:
                    visited[next_r][next_c] = True
                    r, c = next_r, next_c
                    cnt += 1
                    found = True
                    break

        # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우
        if not found:
            next_r, next_c = r - directions[d][0], c - directions[d][1]
            if 0 <= next_r < N and 0 <= next_c < M and grid[next_r][next_c] == 0:
                r, c = next_r, next_c
            else:
                return cnt  
            
def main():
    N, M = map(int, input().split())
    r, c, d = map(int, input().split())
    # 0: 청소되지 않은 빈 칸, 1: 벽
    grid = [list(map(int, input().split())) for _ in range(N)]

    print(simulate(grid, N, M, r, c, d))

if __name__ == '__main__':
    main()