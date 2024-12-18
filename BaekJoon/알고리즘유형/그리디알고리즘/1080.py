# 1080. 행렬
# https://www.acmicpc.net/problem/1080
import sys
N, M = map(int, sys.stdin.readline().split())
A = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
B = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
cnt = 0
flag = True

def convert_matrix(i, j, arr):
    for x in range(i, i + 3):
        for y in range(j, j + 3):
            arr[x][y] = 1 - arr[x][y]

for i in range(N - 2):
    for j in range(M - 2):
        if A[i][j] != B[i][j]:
            convert_matrix(i, j, A)
            cnt += 1
for i in range(N):
    for j in range(M):
        if A[i][j] != B[i][j]:
            flag = False
print(-1 if not flag else cnt)
