# 백준 11726. 2 x n 타일링
# https://www.acmicpc.net/problem/11726
################################ 문제 이해 ################################
# 2 x n 크기의 직사각형을 1 x 2, 2 x 1 타일로 채우는 방법의 수를 구해라.

# 점화식: f(n) = f(n - 1) + f (n - 2)
################################ 문제 이해 ################################
# Top-Down
import sys
sys.setrecursionlimit(10 ** 6)
def sol(n):
    global memo
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n in memo:
        return memo[n]
    
    memo[n] = sol(n - 1) + sol(n - 2)
    return memo[n] % 10007

def main():
    global memo
    n = int(input().strip())
    memo = {}
    print(sol(n))

if __name__ == '__main__':
    main()

# Bottom-Up
def sol(n):
    tab = [0] * (n + 1)
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    tab[1] = 1
    tab[2] = 2

    for i in range(3, n + 1):
        tab[i] = tab[i - 1] + tab[i - 2]
    
    return tab[n] % 10007

def main():
    n = int(input().strip())
    print(sol(n))

if __name__ == '__main__':
    main()