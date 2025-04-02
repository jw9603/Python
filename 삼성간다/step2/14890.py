# 백준 14890. 경사로
# https://www.acmicpc.net/problem/14890


# 길을 지나갈 수 있으려면 길에 속한 모든 칸의 높이가 모두 같아야 한다.
# 경사로는 높이가 항상 1이며, 길이는 L
# 경사로는 낮은 칸과 높은 칸을 연결하며, 아래 조건을 만족해야한다.

# 경사로는 낮은 칸에 놓으며, L개의 연속된 칸에 경사로의 바닥이 모두 접해야 한다.
# 낮은 칸과 높은 칸의 높이 차이는 1이어야 한다.
# 경사로를 놓을 낮은 칸의 높이는 모두 같아야 하고, L개의 칸이 연속되어 있어야 한다.
def can_pass(line, L):
    N = len(line)
    visited = [False] * N

    for i in range(N - 1):
        if line[i] == line[i + 1]:
            continue

        elif line[i] + 1 == line[i + 1]:
            for j in range(i, i - L, -1):
                if j < 0 or line[j] != line[i] or visited[j]:
                    return False
                visited[j] = True

        elif line[i] - 1 == line[i + 1]:
            for j in range(i + 1, i + 1 + L):
                if j >= N or line[j] != line[i + 1] or visited[j]:
                    return False
                visited[j] = True
        else:
            return False
    return True

def cnt_pass(grid, L):
    cnt = 0

    for row in grid:
        if can_pass(row, L):
            cnt += 1
    
    for col in zip(*grid):
        if can_pass(col, L):
            cnt += 1
    
    return cnt

def main():
    N, L = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]

    print(cnt_pass(grid, L))

if __name__ == '__main__':
    main()