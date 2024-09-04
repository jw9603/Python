# 10799 쇠막대기
# https://www.acmicpc.net/problem/10799


# 나만의 문제 이해

# 모든 ()는 레이저를 표현한다.
# 쇠막대기의 왼쪽 끝은 '(', 오른쪽 끝은 ')로 표현된다.
# ()(((()())(())()))(())

import sys
from collections import deque

stick = sys.stdin.readline().strip()
stack = deque()

cnt = 0

for i in range(len(stick)):
    if stick[i] == '(':
        stack.append(i)
    else:
        if stick[i-1] == '(':
            stack.pop()
            cnt += len(stack)
        else: # stick[i-1] == ')'
            stack.pop()
            cnt += 1
print(cnt)
            