def max_coin_cnt(n, grid):
    cnt = 0

    for i in range(n - 2):
        for j in range(n - 2):
            mid_cnt = 0
            for k in range(i, i + 3):
                for m in range(j, j + 3):
                    mid_cnt += grid[k][m]
            cnt = max(cnt, mid_cnt)
    
    return cnt

def main():
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]

    print(max_coin_cnt(n=n, grid=grid))

if __name__ == '__main__':
    main()