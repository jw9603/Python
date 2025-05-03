# 백준 1051. 숫자 정사각형
# https://www.acmicpc.net/problem/1051
################################# 문제 이해 #################################
# N x M 크기의 직사각형이 있다. 각 칸에는 한 자리 숫자가 적혀 있다.
# 이 직사각형에서 꼭짓점에 쓰여 있는 수가 모두 같은 가장 큰 정사각형을 찾는 프로그램 작성
# N과 M이 주어진다. N과 M은 50이하의 자연수.
################################# 문제 이해 #################################
def find_square(N, M, s, grid):
    for i in range(N - s + 1):
        for j in range(M - s + 1):
            if grid[i][j] == grid[i][j + s - 1] == grid[i + s - 1][j] == grid[i + s - 1][j + s - 1]:
                return True
    
    return False

def main():
    N, M = map(int, input().split())
    grid = [list(map(int, input().strip())) for _ in range(N)]
    S = min(N, M)
    
    for s in range(S, 0, -1):
        if find_square(N, M, s, grid):
            print(s ** 2)
            break

if __name__ == '__main__':
    main()