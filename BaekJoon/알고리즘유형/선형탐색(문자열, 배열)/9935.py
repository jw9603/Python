# 백준 9935. 문자열 폭발
# https://www.acmicpc.net/problem/9935
import sys
s = sys.stdin.readline().strip()
explosion = sys.stdin.readline().strip()
def sol(s, explosion):
    e = len(explosion)
    stack = []
    for i in s:
        stack.append(i)
        if len(s) >= e and ''.join(stack[-e:]) == explosion:
            for _ in range(e):
                stack.pop()
    print(''.join(stack) if stack else "FRULA")
sol(s=s, explosion=explosion)