# 백준 1932. 정수 삼각형
# https://www.acmicpc.net/problem/1932
################################## 문제 이해 ##################################
# 맨 위층에서부터 시작하여 아래층으로 내려올 때, 이제까지 선택된 수의 합이 최대가 되는
# 경로를 구해라.
# 아래층에 있는 수는 현재 층에서 선택된 수의 대각선 왼쪽 또는 대각선 오른쪽에 있는 것 중에서만 선택할 수 있다.

################################## 문제 이해 ##################################
def sol(n, tri):
    tab = [[0] * n for _ in range(n)]
    tab[0][0] = tri[0][0]

    for i in range(1, n):
        for j in range(i + 1):
            if j == 0:
                tab[i][j] = tri[i][j] + tab[i - 1][j]
            elif i == j:
                tab[i][j] = tri[i][j] + tab[i - 1][j - 1]
            else:
                tab[i][j] = tri[i][j] + max(tab[i - 1][j - 1], tab[i - 1][j])

    return max(tab[n - 1])

def main():
    n = int(input().strip())
    tri = [list(map(int, input().split())) for _ in range(n)]

    print(sol(n, tri))

if __name__ == '__main__':
    main()