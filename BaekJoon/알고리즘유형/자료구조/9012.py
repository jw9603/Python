# 백준 9012. 괄호
# https://www.acmicpc.net/problem/9012
import sys
T = int(sys.stdin.readline().strip())
for _ in range(T):
    vps = sys.stdin.readline().strip()
    stack = []
    for ps in vps:
        if ps == '(':
            stack.append(ps)
        else: # ps == ')'
            if stack:
                stack.pop()
            else: # stack이 비어있을때
                stack.append(ps)
                break
    print('YES' if not stack else 'NO')