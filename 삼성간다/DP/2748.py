# 백준 2748. 피보나치 수 2
# https://www.acmicpc.net/problem/2748

############################## 1. 완전 탐색 ##############################
import sys
def fibo(n):
    # 1. base case
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    
    # 2. 재귀 호출
    mid = fibo(n - 1) + fibo(n - 2)
    
    # 3. 데이터 통합
    return mid

def main():
    n = int(sys.stdin.readline().strip())
    print(fibo(n))

if __name__ == '__main__':
    main()
############################## 1. 완전 탐색 ##############################

############################## 2. Top-Down ##############################
import sys
memo = {}
def fibo(n):
    # 1. base case
    if n == 0:
        return 0
    if n == 1 or n== 2:
        return 1
    
    if n in memo:
        return memo[n]
    
    memo[n] = fibo(n - 1) + fibo(n - 2)
    return memo[n]

def main():
    n = int(sys.stdin.readline().strip())
    print(fibo(n))

if __name__ == '__main__':
    main()
############################## 2. Top-Down ##############################

############################## 3. Bottom-Up ##############################
import sys

def fibo(n):
    tab = [-1] * (n + 1)
    tab[0] = 0
    tab[1] = 1
    for i in range(2, n + 1):
        tab[i] = tab[i - 1] + tab[i - 2]
    return tab[n]

def main():
    n = int(sys.stdin.readline().strip())
    print(fibo(n))

if __name__ == '__main__':
    main()
############################## 3. Bottom-Up ##############################