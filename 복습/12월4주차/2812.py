# 백준 2812. 크게 만들기
# https://www.acmicpc.net/problem/2812
import sys
N, K = map(int, sys.stdin.readline().split())
num = sys.stdin.readline().strip()
def sol(N, k, num):
    stack = []
    i = 0
    for n in num:
        while stack and i < k and stack[-1] < n:
            i += 1
            stack.pop()
        stack.append(n)
    # print(''.join(stack[:N-k]))
    print(stack)
sol(N=N, k=K, num=num)        