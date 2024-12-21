# 백준 11047. 동전 0
# https://www.acmicpc.net/problem/11047
import sys
N, K = map(int, sys.stdin.readline().split())
coins = list(int(sys.stdin.readline().strip()) for _ in range(N))
def sol(N, K, coins):
    cnt = 0
    for i in range(N-1, -1, -1):
        cnt += K // coins[i]
        K %= coins[i]
    print(cnt)
sol(N=N, K=K, coins=coins)