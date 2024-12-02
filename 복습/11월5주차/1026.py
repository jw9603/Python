# 1026. 보물
# https://www.acmicpc.net/problem/1026

import sys

N = int(sys.stdin.readline().strip())

A = list(map(int,sys.stdin.readline().split()))
B = list(map(int,sys.stdin.readline().split()))

def sol(A, B):
    A.sort()
    B.sort(reverse=True)
    
    result = 0
    for i in range(N):
        result += A[i] * B[i]
    return result
print(sol(A=A, B= B))