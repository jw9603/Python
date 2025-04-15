# 백준 1463. 1로 만들기
# https://www.acmicpc.net/problem/1463
################################ 문제 이해 ################################
# 정수 X에 사용할 수 있는 연산은 3가지
# 1. X가 3으로 나누어 떨어지면, 3으로 나눈다.
# 2. X가 2로 나누어 떨어지면, 2로 나눈다.
# 3. 1을 뺀다.

# 정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다.
# 연산을 사용하는 횟수의 최솟값을 출력.
################################ 문제 이해 ################################

################################ 완전 탐색 (시간 초과)################################
# def dfs(N, cnt):
#     # 1. base case
#     if N == 1:
#         return cnt
    
#     res = dfs(N - 1, cnt + 1)

#     if N % 2 == 0:
#         res = min(res, dfs(N // 2, cnt + 1))
#     if N % 3 == 0:
#         res = min(res, dfs(N // 3, cnt + 1))
    
#     return res

# def main():
#     N = int(input().strip())

#     print(dfs(N, 0))

# if __name__ == '__main__':
#     main()
################################ 완전 탐색 ################################
################################ Top-Down ################################
import sys
sys.setrecursionlimit(10 ** 6)
def dfs(N):
    global memo

    # 1. base case
    if N == 1:
        return 0
    
    if N in memo:
        return memo[N]
    
    res = dfs(N - 1) + 1

    if N % 2 == 0:
        res = min(res, dfs(N // 2) + 1)
    if N % 3 == 0:
        res = min(res, dfs(N // 3) + 1)
    
    memo[N] = res
    return memo[N]

def main():
    global memo
    N = int(input().strip())
    memo = {}
    print(dfs(N))

if __name__ == '__main__':
    main()
################################ Top-Down ################################

################################ Bottum-Up ################################
def dfs(N):
    tab = [0] * (N + 1)

    for i in range(2, N + 1):
        tab[i] = tab[i - 1] + 1

        if i % 2 == 0:
            tab[i] = min(tab[i], tab[i // 2] + 1)
        if i % 3 == 0:
            tab[i] = min(tab[i], tab[i // 3] + 1)

    return tab[N]

def main():
    N = int(input().strip())
    print(dfs(N))

if __name__ == '__main__':
    main()
################################ Bottom-Up ################################
