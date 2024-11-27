# 1439. 뒤집기
# https://www.acmicpc.net/problem/1439

import sys

S = sys.stdin.readline().strip()

def sol(S):
    cnt = 0
    for i in range(len(S)-1):
        if S[i+1] != S[i]:
            cnt += 1
    return (cnt+1) // 2

print(sol(S=S))
    