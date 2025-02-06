# 백준 1463. 1로 만들기
# https://www.acmicpc.net/problem/1463
#################### 완전 탐색 #####################
# import sys
# N = int(sys.stdin.readline().strip())
# def sol(N, cnt):
#     # 1. base case
#     if N == 1:
#         return cnt
    
#     # 2. 재귀 호출
#     res = sol(N - 1, cnt + 1) 
    
#     if N % 2 == 0:
#         res = min(res, sol(N // 2, cnt + 1))
#     if N % 3 == 0:
#         res = min(res, sol(N // 3, cnt + 1))
    
#     return res
    

# print(sol(N=N, cnt=0))
#################### 완전 탐색 #####################

#################### Top-Down ####################
import sys
sys.setrecursionlimit(10**6)
N = int(sys.stdin.readline().strip())
memo = {}
def sol(n, memo):
    if n == 1:
        return 0
    if n in memo:
        return memo[n]
    
    res = sol(n - 1, memo) + 1
    
    if n % 2 == 0:
        res = min(res, sol(n // 2, memo) + 1)
    if n % 3 == 0:
        res = min(res, sol(n // 3, memo) + 1)
    memo[n] = res
    
    return memo[n]
print(sol(n=N, memo=memo))
#################### Top-Down ####################

################### Bottom-UP ####################
import sys
N = int(sys.stdin.readline().strip())
def sol(n):
    tab = [0] * (n + 1)
    
    for i in range(2, n + 1):
        tab[i] = tab[i - 1] + 1
        
        if i % 2 == 0:
            tab[i] = min(tab[i], tab[i // 2] + 1)
        if i % 3 == 0:
            tab[i] = min(tab[i], tab[i // 3] + 1)
    return tab[n]
print(sol(n=N))
# ################### Bottom-UP ####################