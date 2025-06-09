# 백준 16918. 봄버맨
# https://www.acmicpc.net/problem/16918
############################# 문제 이해 #############################
# R X C인 직사각형, 격자의 각 칸은 비어있거나 폭탄

# 폭탄이 있는 칸은 3초가 지난 후에 폭발, 폭탄이 폭발한 이후에는 폭탄이 있던 칸이
# 파괴되어 빈 칸이 되며, 인접한 네 칸도 함께 파괴된다.

# 만약, 폭탄이 폭발했을 때, 인접한 칸에 폭탄이 있는 경우에는 인접한 폭탄은 폭발 없이 파괴된다.
# 따라서, 연쇄 반응은 X
# 봄버맨은 폭탄에 면역력을 가지고 있어서, 격자판의 몬든 칸을 자유롭게 이동할 수 있다.
# 봄버맨은 다음과 같이 행동한다.
# 1. 가장 처음에 봄버맨은 일부 칸에 폭탄을 설치해 놓는다. (0초)
# 2. 다음 1초동안 아무것도 하지 않는다. (1초)
# 3. 다음 1초동안 폭탄이 설치되어 잇지 않은 모든 칸에 폭탄을 설치  (2초)
# 4. 처음에 설치했던 폭탄이 모두 폭발한다. (3과 4를 반복한다.)

# Input:
# 첫째 줄에 R, C, N이 주어진다.
# 빈 칸은 '.', 폭탄은 'O'로 주어진다.
############################# 문제 이해 #############################
def explode(r, c, base_grid):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    new_grid = [['O'] * c for _ in range(r)]
    
    for x in range(r):
        for y in range(c):
            if base_grid[x][y] == 'O':
                new_grid[x][y] = '.'
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < r and 0 <= ny < c:
                        new_grid[nx][ny] = '.'
    
    return new_grid

def simulate(r, c, n, grid):
    # 1. 그대로 출력
    if n == 1:
        return [''.join(row) for row in grid]
     
    # 2. 2초마다 모든 칸에 폭탄 설치
    if n % 2 == 0:
        return ['O' * c for _ in range(r)]
    
    # 3. 폭탄 터지기
    bomb1 = explode(r, c, grid)
    bomb2 = explode(r, c, bomb1)

    return [''.join(row) for row in (bomb1 if n % 4 == 3 else bomb2)]

def main():
    R, C, N = map(int, input().split())
    grid = [list(input().strip()) for _ in range(R)]

    result = simulate(r=R, c=C, n=N, grid=grid)
    for row in result:
        print(row)

if __name__ == '__main__':
    main()