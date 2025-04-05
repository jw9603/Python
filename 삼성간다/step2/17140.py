# 백준 17140. 이차원 배열과 연산
# https://www.acmicpc.net/problem/17140

# 크기가 3 x 3인 배열 A가 있다. 배열의 인덱스는 1부터 시작
# 1초가 지날때마다 배열에 연산이 적용된다.
# R 연산: 배열 A의 모든 행에 대해서 정렬을 수행한다. 행의 개수 >= 열의 개수인 경우에 적용
# C 연산: 배열 A의 모든 열에 대해서 정렬을 수행한다. 행의 개수 < 열의 개수인 경우에 적용
from collections import Counter
def operate_r(grid):
    max_len = 0
    new_board = []

    for row in grid:
        counter = Counter([num for num in row if num != 0])
        sorted_row = []
        for num, cnt in sorted(counter.items(), key=lambda x:(x[1], x[0])):
            sorted_row.extend([num, cnt])
        max_len = max(max_len, len(sorted_row))
        new_board.append(sorted_row)
    
    # 정렬된 결과를 배열에 다시 넣으면 행 또는 열의 크기가 달라질 수 있다.
    # R 연산이 적용된 경우에는 가장 큰 행을 기준으로 모든 행의 크기가 변한다.
    # 차이만큼 0이 채워짐
    for row in new_board:
        while len(row) < max_len:
            row.append(0)
        row[:] = row[:100]
    return new_board

def operate_c(grid):

    transposed = list(zip(*grid))
    transposed = [list(col) for col in transposed]
    
    operated = operate_r(transposed)
    return [list(row) for row in zip(*operated)]

def main():
    r, c, k = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(3)]

    for time in range(101):
        if 0 <= r - 1 < len(grid) and 0 <= c - 1 < len(grid[0]):
            if grid[r - 1][c - 1] == k:
                print(time)
                return
            
        if len(grid) >= len(grid[0]):
            grid = operate_r(grid)
        else:
            grid = operate_c(grid)
            
    print(-1)

if __name__ == '__main__':
    main()