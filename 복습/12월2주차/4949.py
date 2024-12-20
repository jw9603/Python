# 4949. 균형잡힌 세상
# https://www.acmicpc.net/problem/4949
import sys

while True:
    text = sys.stdin.readline().rstrip()
    if text == '.':
        break
    stack = []
    flag = True
    for t in text:
        if t == '(' or t == '[':
            stack.append(t)
        elif t == ')':
            if not stack or stack[-1] == '[':
                flag = False
                break
            stack.pop()
        elif t == ']':
            if not stack or stack[-1] == '(':
                flag = False
                break
            stack.pop()
    print('yes' if not stack and flag else 'no')
                