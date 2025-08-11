# 백준 1463. 1로 만들기
# https://www.acmicpc.net/problem/1463
################################### 문제 이해 ###################################
# 정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.
# 1. X가 3으로 나누어 떨어지면, 3으로 나눈다.
# 2. X가 2로 나누어 떨어지면, 2로 나눈다.
# 3. 1을 뺀다.
# 정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다.
# 연산을 사용하는 횟수의 최솟값을 출력해라

# 입력: 정수 N이 주어진다.
# 출력: 연산을 하는 횟수의 최솟값을 출력

# 알고리즘
# 연산을 수행하면서 최솟값을 구하는 완전탐색으로 풀 수 있다.
# 하지만, 정수 N의 범위가 10^6이하의 자연수이므로, 완탐-> O(3^n)으로 시간초과
# 그렇다면? DP

################################### 문제 이해 ###################################
# # 1. 완전 탐색
# def sol(N, cnt):
#     # 1. base case:
#     if N == 1:
#         return cnt
    
#     # 2. 재귀 호출
#     res = sol(N - 1, cnt + 1)

#     if N % 2 == 0:
#         res = min(res, sol(N // 2, cnt + 1))
#     if N % 3 == 0:
#         res = min(res, sol(N // 3, cnt + 1))
    
#     return res

# def main():
#     N = int(input().strip())
#     print(sol(N, 0))

# if __name__ == '__main__':
#     main()

# 2. Top-Down
import sys
sys.setrecursionlimit(10 ** 6)
def sol(N, memo):
    # 1. base case
    if N == 1:
        return 0
    
    if N in memo:
        return memo[N]

    res = sol(N - 1, memo) + 1

    if N % 2 == 0:
        res = min(res, sol(N // 2, memo) + 1)
    if N % 3 == 0:
        res = min(res, sol(N // 3, memo) + 1)

    memo[N] = res

    return res

def main():
    N = int(input().strip())
    memo = {}
    print(sol(N, memo))

if __name__ == '__main__':
    main()

# 3. Bottom-Up
def sol(N):
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
    print(sol(N))

if __name__ == '__main__':
    main()