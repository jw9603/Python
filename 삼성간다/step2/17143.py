# 백준 17143. 낚시왕
# https://www.acmicpc.net/problem/17143

# 낚시왕은 처음에 1번 열의 한 칸 왼쪽에 있다.
# 아래 순서대로 일어나며 1초 동안 일어나는 일이다. 낚시왕은 가장 오른쪽 열의 오른쪽 칸에 이동하면 멈춘다.

# 1. 낚시왕이 오른쪽으로 한 칸 이동
# 2. 낚시왕이 있는 열에 있는 상어 중에서 땅과 제일 가까운 상어를 잡는다. 상어를 잡으면 격자판에서 잡은 상어가 사라짐
# 3. 상어가 이동한다.


# 상어는 입력으로 주어진 속도로 이동하고, 속도의 단위는 칸/초
# 상어가 이동하려고 하는 칸이 격자판의 경계를 넘는 경우에는 방향을 반대로 바꿔서 속력을 유지한채로 이동한다.
from collections import defaultdict
def fishing_king(R, C, sharks):

    directions = [(0, 0), (-1, 0), (1, 0), (0, 1), (0, -1)]
    grid = defaultdict(list)

    for r, c, s, d, z in sharks:
        # s: 속력, d: 이동 방향, z: 크기
        grid[(r - 1, c - 1)] = [s, d, z]

    total = 0

    for fisher_col in range(C): # 낚시왕은 왼쪽에서 오른쪽으로 한 칸씩 이동
        target = None
        # 1. 상어를 잡는다.
        for row in range(R):
            if (row, fisher_col) in grid:
                target = (row, fisher_col)
                break
        
        if target:
            total += grid[target][2]
            del grid[target] # 상어를 잡으면 격자판에서 잡은 상어가 사라짐
        
        # 2. 상어가 이동
        new_grid = defaultdict(list)
        for (x, y), (s, d, z) in grid.items():
            cur_x, cur_y, cur_d = x, y, d
            speed = s

            if cur_d in [1, 2]:
                speed %= (2 * (R - 1))
            else:
                speed %= (2 * (C - 1))
            
            for _ in range(speed):
                nx = cur_x + directions[cur_d][0]
                ny = cur_y + directions[cur_d][1]

                if not (0 <= nx < R and 0 <= ny < C):
                    if cur_d == 1:
                        cur_d = 2
                    elif cur_d == 2:
                        cur_d = 1
                    elif cur_d == 3:
                        cur_d = 4
                    elif cur_d == 4:
                        cur_d = 3
                    
                    nx = cur_x + directions[cur_d][0]
                    ny = cur_y + directions[cur_d][1]

                cur_x, cur_y = nx, ny
            
            if new_grid[(cur_x, cur_y)]:
                if new_grid[(cur_x, cur_y)][2] < z:
                    new_grid[(cur_x, cur_y)] = [s, cur_d, z]
            else:
                new_grid[(cur_x, cur_y)] = [s, cur_d, z]

        grid = new_grid

    return total
                
def main():
    R, C, M = map(int, input().split())
    sharks = [tuple(map(int, input().split())) for _ in range(M)]
    
    print(fishing_king(R, C, sharks))

if __name__ == '__main__':
    main()