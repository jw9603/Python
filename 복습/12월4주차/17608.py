# 백준 17608. 막대기
# https://www.acmicpc.net/problem/17608
import sys
N = int(sys.stdin.readline().strip())
sticks = [int(sys.stdin.readline().strip()) for _ in range(N)]
def sol(N, sticks):
    cnt = 1
    stack = sticks[-1]
    for i in range(N - 1, -1, -1):
        if stack < sticks[i]:
            cnt += 1
            stack = sticks[i]
    print(cnt)
sol(N=N, sticks=sticks)