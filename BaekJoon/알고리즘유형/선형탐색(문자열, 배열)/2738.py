# 백준 2738. 행렬 덧셈
# https://www.acmicpc.net/problem/2738
import sys
N, M = map(int, sys.stdin.readline().split())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
B = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

for i in range(N):
    result = []
    for j in range(M):
        result.append(A[i][j] + B[i][j])
    print(*result)    