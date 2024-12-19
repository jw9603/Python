# 백준 11047. 동전 0
# https://www.acmicpc.net/problem/11047
import sys
N, K = map(int, sys.stdin.readline().split())
value = [int(sys.stdin.readline().strip()) for _ in range(N)]

def sol(N, K, value):
    cnt = 0
    for i in range(N - 1, -1, -1):
        cnt += K // value[i]
        K %= value[i]
    return cnt
print(sol(N=N, K=K, value=value))