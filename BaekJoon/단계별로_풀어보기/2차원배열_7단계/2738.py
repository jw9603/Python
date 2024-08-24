# 2차원 배열 2738번
# https://www.acmicpc.net/problem/2738

import sys

N, M = map(int,sys.stdin.readline().split())
A, B = [], []
for _ in range(N):
    f = list(map(int,sys.stdin.readline().split()))
    A.append(f)
for _ in range(N):
    s = list(map(int,sys.stdin.readline().split()))
    B.append(s)
    
for i in range(N):
    for j in range(M):
        result = A[i][j] + B[i][j]
        print(result,end= ' ')
    print()