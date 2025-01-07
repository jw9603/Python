# 백준 10870. 피보나치 수 5
# https://www.acmicpc.net/problem/10870
import sys
n = int(sys.stdin.readline().strip())
def sol(n):
    # 1. base case
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    # 2. 재귀 호출
    n_1 = sol(n - 1)
    n_2 = sol(n - 2)
    
    # 3. 데이터 통합
    return n_1 + n_2
print(sol(n=n))