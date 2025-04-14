# 백준 2748. 피보나치 수 2
# https://www.acmicpc.net/problem/2748
###################### 완전 탐색 ######################
def fibo(n):
    # 1. base case
    if n == 1:
        return 1
    if n == 0:
        return 0
    
    return fibo(n - 1) + fibo(n - 2)

def main():
    n = int(input().strip())
    print(fibo(n))

if __name__ == '__main__':
    main()
###################### 완전 탐색 ######################

###################### Top-Down ######################
def fibo(n):
    global memo
    # 1. base case
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n in memo:
        return memo[n]

    memo[n] = fibo(n - 1) + fibo(n - 2)
    return memo[n]

def main():
    global memo
    n = int(input().strip())
    memo = {}
    print(fibo(n))

if __name__ == '__main__':
    main()
###################### Top-Down ######################

###################### Bottom-Up ######################
def fibo(n):
    memo = [0] * (n + 1)
    memo[1] = 1

    for i in range(2, n + 1):
        memo[i] = memo[i - 1] + memo[i - 2]
    return memo[n]

def main():
    n = int(input().strip())
    print(fibo(n))

if __name__ == '__main__':
    main()
###################### Bottom-Up ######################