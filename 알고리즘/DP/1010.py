# 백준 1010. 다리 놓기
# https://www.acmicpc.net/problem/1010
############################## 문제 이해 ##############################
# 강 주변에서 다리를 짓기에 적합한 곳을 사이트라고 한다.
# 강의 서쪽에는 N개의 사이트, 동쪽에는 M개의 사이트가 있다. (N <= M)
# 다리끼리는 서로 겹쳐질 수 없다고 할 때 다리를 지을 수 있는 경우의 수

# 입력
# 첫 줄에는 테스트 케이스의 개수 T
# 그 다음 줄부터 각각의 테스트케이스에 대해 강의 서쪽과 동쪽에 있는 사이트의 개수 정수 N, M
# 이 주어진다.
############################## 문제 이해 ###############################
# 1. 조합 방식
# from itertools import combinations
# def sol(n, m):
#     return len(list(combinations(range(m), n)))

# def main():
#     T = int(input().strip())
#     for _ in range(T):
#         N, M = map(int, input().split())
#         print(sol(N, M))

# if __name__ == '__main__':
#     main()

# 2. DP
def sol(N, M):
    tab = [[0]* 31 for _ in range(31)]

    for n in range(31):
        for r in range(31):
            if r == 0 or n == r:
                tab[n][r] = 1
            else:
                tab[n][r] = tab[n - 1][r - 1] + tab[n - 1][r]
    return tab[M][N]

def main():
    T = int(input().strip())
    for _ in range(T):
        N, M = map(int, input().split())
        print(sol(N, M))

if __name__ == '__main__':
    main()
