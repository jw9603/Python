# 백준 2493. 탑
# https://www.acmicpc.net/problem/2493
import sys
N = int(sys.stdin.readline().strip())
towers = list(map(int, sys.stdin.readline().split()))
result = [0] * N
stack = []
for i in range(N):
    while stack and stack[-1][1] < towers[i]:
        stack.pop()
    if stack:
        result[i] = stack[-1][0]
    stack.append((i + 1, towers[i]))
print(' '.join(map(str, result)))