# 17103. 골드바흐 파티션
# https://www.acmicpc.net/problem/17103
import sys

def sol(n):
    
    is_prime = [False] * 2 + [True] * (n - 1)
    
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return is_prime

def sol_cnt(n,is_prime):
    cnt = 0

    for i in range(2, n // 2 + 1):
        if result[i] and result[n-i]:
            cnt += 1
    return cnt
    
T = int(sys.stdin.readline().strip())
result = sol(10**6)

for _ in range(T):
    N = int(sys.stdin.readline().strip())
    print(sol_cnt(n=N, is_prime=result))
    
    