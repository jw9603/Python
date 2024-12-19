# 백준 9012. 괄호
# https://www.acmicpc.net/problem/9012
import sys
T = int(sys.stdin.readline().strip())
for _ in range(T):
    vps = sys.stdin.readline().strip()
    stack = []
    for p in vps:
        if p == '(':
            stack.append(p)
        else:
            if stack:
                stack.pop()
            else:
                stack.append(p)
                break
    print('YES' if not stack else 'NO')
    