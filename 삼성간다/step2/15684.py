# 백준 15684. 사다리 조작
# https://www.acmicpc.net/problem/15684
def can_place(ladder, i, j, N):
    if ladder[i][j]:
        return False
    
    if j > 0 and ladder[i][j - 1]:
        return False
    if j < N - 2 and ladder[i][j + 1]:
        return False

    return True

def simulate(H, N, ladder):
    # N은 세로선, M개의 가로선, H: 가로선을 놓을 수 있는 위치
    for start in range(N):
        k = start

        for row in range(H):
            if k < N - 1 and ladder[row][k]:   # 오른쪽으로 가는 가로선이 있다면
                k += 1
            elif k > 0 and ladder[row][k - 1]: # 왼쪽으로 가는 가로선이 있다면
                k -= 1

        if k != start:
            return False
        
    return True

def dfs(depth, N, H, ladder, row, col):
    global result

    if depth >= result:
        return
    
    if simulate(H, N, ladder):
        result = depth
        return
    
    if depth == 3:
        return
    
    for i in range(row, H):
        sj = col if i == row else 0
        for j in range(sj, N - 1):
            if can_place(ladder, i, j, N):
                ladder[i][j] = True
                dfs(depth + 1, N, H, ladder, i, j + 2)
                ladder[i][j] = False

def sol(N, M, H):
    global result
    ladder = [[False] * (N - 1) for _ in range(H)]
    for _ in range(M):
        a, b = map(int, input().split())
        ladder[a - 1][b - 1] = True
    
    result = 4
    dfs(0, N, H, ladder, 0, 0)
    
    return result if result <= 3 else -1

def main():
    N, M, H = map(int, input().split())

    print(sol(N, M, H))

if __name__ == '__main__':
    main()