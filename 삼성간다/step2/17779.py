# 백준 17779. 게리맨더링 2
# https://www.acmicpc.net/problem/17779

def in_range(x, y, N):
    return 0 <= x < N and 0 <= y < N

def possible_to_draw(x, y, d1, d2, n):
    return in_range(x - d1, y + d1, n) and in_range(x - d1 - d2, y + d1 - d2, n) and in_range(x - d2, y - d2, n)

def mark_boundary(x, y, d1, d2, n):

    border = [[False] * n for _ in range(n)]

    dxs = [-1, -1, 1, 1]
    dys = [1, -1, -1, 1]
    move_nums = [d1, d2, d1, d2]

    for dx, dy, move_num in zip(dxs, dys, move_nums):
        for _ in range(move_num):
            x += dx
            y += dy
            border[x][y] = True
    
    return border

def divide_sections(x, y, d1, d2, border, n, A, total_sum):
    sections = [0] * 5

    # 2번 구역(좌측 상단)
    for i in range(x - d2):
        for j in range(y + d1 - d2 + 1):
            if border[i][j]:
                break
            sections[1] += A[i][j]
    
    # 3번 구역 (우측 상단)
    for i in range(x - d1 + 1):
        for j in range(n - 1, y + d1 - d2, -1):
            if border[i][j]:
                break
            sections[2] += A[i][j]
    
    # 4번 구역 (좌측 하단)
    for i in range(x - d2, n):
        for j in range(y):
            if border[i][j]:
                break
            sections[3] += A[i][j]
    
    # 5번 구역 (우측 하단)
    for i in range(x - d1 + 1, n):
        for j in range(n - 1, y - 1, -1):
            if border[i][j]:
                break
            sections[4] += A[i][j]
    
    # 1번 구역: 전체 인구에서 나머지 네 부족을 빼면 됨
    sections[0] = total_sum - sum(sections[1:])

    return max(sections) - min(sections)

def calculate_population_diff(n, A):
    total_sum = sum(sum(row) for row in A)
    min_diff = float('inf')

    for x in range(n):
        for y in range(n):
            for d1 in range(1, n):
                for d2 in range(1, n):
                    if possible_to_draw(x, y, d1, d2, n):
                        border = mark_boundary(x, y, d1, d2, n)
                        diff = divide_sections(x, y, d1, d2, border, n, A, total_sum)
                        min_diff = min(min_diff, diff)

    return min_diff

def main():
    n = int(input().strip())
    A = [list(map(int, input().split())) for _ in range(n)]
    print(calculate_population_diff(n, A))

if __name__ == '__main__':
    main()