# 백준 17413. 단어 뒤집기 2
# https://www.acmicpc.net/problem/17413
import sys
S = sys.stdin.readline().strip()
def sol(S):
    stack = []
    result = ''
    tag = False
    for i in S:
        if i == '<':
            while stack:
                result += stack.pop()
            tag = True
            result += i
        elif i == '>':
            tag = False
            result += i
        elif tag:
            result += i
        elif i == ' ':
            while stack:
                result += stack.pop()
            result += i
        else:
            stack.append(i)
    return result + ''.join(stack[::-1]) if stack else result
print(sol(S=S))
        