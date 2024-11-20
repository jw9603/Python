# 2748. 피보나치 수 2
# https://www.acmicpc.net/problem/2748

import sys

n = int(sys.stdin.readline().strip())

# Top-Down
memo = {}
def fibo_topdown(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n in memo:
        return memo[n]
    
    memo[n] = fibo_topdown(n - 1) + fibo_topdown(n - 2)
    return memo[n]
# Botton-Up
def fibo_bottomup(n):
    dp = [0] * (n + 1)
    dp[1] = 1
    
    for i in range(2,n+1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

print(fibo_topdown(n))
print(fibo_bottomup(n))