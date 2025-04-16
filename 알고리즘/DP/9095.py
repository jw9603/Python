# 백준 9095. 1, 2, 3 더하기
# https://www.acmicpc.net/problem/9095
################################ 문제 이해 ################################
# 정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구해.

################################ 문제 이해 ################################ 

################################ 완전 탐색 ################################ 
def sol(n):
    # 1. base case
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    
    res = sol(n - 1) + sol(n - 2) + sol(n - 3)

    return res

def main():
    T = int(input().strip())
    for _ in range(T):
        n = int(input().strip())
        print(sol(n))

if __name__ == '__main__':
    main()
################################ 완전 탐색 ################################

################################ Top-Down ################################
def sol(n):
    global memo

    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    
    if n in memo:
        return memo[n]

    res = sol(n - 1) + sol(n - 2) + sol(n - 3)
    memo[n] = res

    return memo[n]

def main():
    global memo
    T = int(input().strip())
    for _ in range(T):
        n = int(input().strip())
        memo = {}
        print(sol(n))

if __name__ == '__main__':
    main()
################################ Top-Down ################################
 
################################ Bottom-Up ################################
def sol(n):
    tab = [0] * (n + 1)
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    tab[1] = 1
    tab[2] = 2
    tab[3] = 4

    for i in range(4, n + 1):
        tab[i] = tab[i - 1] + tab[i - 2] + tab[i - 3]
    
    return tab[n]

def main():
    T = int(input().strip())

    for _ in range(T):
        n = int(input().strip())
        print(sol(n))

if __name__ == '__main__':
    main() 
################################ Bottom-Up ################################ 