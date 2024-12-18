# 2493. 탑
# https://www.acmicpc.net/problem/2493
import sys
N = int(sys.stdin.readline().strip())
towers = list(map(int, sys.stdin.readline().split()))
def sol(N, towers):
    stack = []
    result = [0] * N
    for t in range(N):
        while stack and stack[-1][1] < towers[t]:
            stack.pop()
        if stack:
            result[t] = stack[-1][0]
        stack.append((t + 1, towers[t]))
    return ' '.join(map(str, result))
print(sol(N=N, towers=towers))