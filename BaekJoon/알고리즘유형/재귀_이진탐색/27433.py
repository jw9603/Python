# 백준 27433. 팩토리얼 2
# https://www.acmicpc.net/problem/27433
import sys
N = int(sys.stdin.readline().strip())
def sol(n):
    if n == 0 or n == 1 :
        return 1
    return n * sol(n - 1)
print(sol(n=N))