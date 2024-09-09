# 11047번 - 동전 0
# https://www.acmicpc.net/problem/11047

import sys

def solution(N,K,coin):
    cnt = 0
               
    for i in range(N-1,-1,-1):
        cnt += K // coin[i]
        K %= coin[i]
    return cnt

N, K = map(int,sys.stdin.readline().split())
coin = []
for i in range(N):
    coin.append(int(sys.stdin.readline().strip()))

print(solution(N,K,coin))