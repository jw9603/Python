# 백준 1463. 1로 만들기
# https://www.acmicpc.net/problem/1463
#################### 완전 탐색 #####################
# import sys
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

# def main():
#     N = int(sys.stdin.readline().strip())
#     print(sol(N=N, cnt=0))
# main()
#################### 완전 탐색 #####################

#################### Top-Down(메모리 초과) ####################
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
    N = int(sys.stdin.readline().strip())
    memo = {}
    print(sol(N=N, memo=memo))
main()
#################### Top-Down(메모리 초과) ####################

################### Bottom-UP ####################
import sys
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
    N = int(sys.stdin.readline().strip())
    print(sol(N=N))
main()
#################### Bottom-UP ####################