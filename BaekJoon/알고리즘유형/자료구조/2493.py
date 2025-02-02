# 백준 2493. 탑
# https://www.acmicpc.net/problem/2493
import sys
N = int(sys.stdin.readline().strip())
towers = list(map(int, sys.stdin.readline().split()))
def sol(N, towers):
    result = [0] * N
    stack = []
    
    for idx, tower in enumerate(towers):
        while stack and stack[-1][1] < towers[idx]:
            stack.pop()
            
        if stack:
            result[idx] = stack[-1][0]
        
        stack.append((idx + 1, tower))
    return result
print(*sol(N=N, towers=towers))