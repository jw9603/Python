# 백준 2193. 이친수
# https://www.acmicpc.net/problem/2193
################################# 문제 이해 #################################
# 이진수 중 특별한 성질을 갖는 것들 == 이친수
# 이친수의 특징
# 0으로 시작하지 않는다.
# 이친수에서는 1이 두 번 연속으로 나타나지 않는다.
# N이 주어졌을 때, N자리 이친수의 개수를 구하는 프로그램을 작성.

# 알고리즘
# 1 <= N <= 90
# tab[i] = tab[i - 1] + tab[i - 2]
################################# 문제 이해 #################################
# 1. Bottom-Up
def sol(n):
    tab = [0] * (n + 1)
    if n == 1:
        return 1
    tab[1] = 1

    for i in range(2, n + 1):
        tab[i] = tab[i - 1] + tab[i - 2]

    return tab[n]

def main():
    N = int(input().strip())
    print(sol(N))

if __name__ == '__main__':
    main()

# 2. Top-Down
def sol(n):
    global memo
    if n == 1:
        return 1
    if n == 2:
        return 1
    
    if n in memo:
        return memo[n]

    res = sol(n - 1) + sol(n - 2)
    memo[n] = res

    return memo[n]

def main():
    global memo
    N = int(input().strip())
    memo = {}
    print(sol(N))

if __name__ == '__main__':
    main()