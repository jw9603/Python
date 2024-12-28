# 백준 2504. 괄호의 값
# https://www.acmicpc.net/problem/2504
import sys
s = sys.stdin.readline().strip()
def sol(s):
    
    stack = []
    total = 0
    tmp = 1
    for i, char in enumerate(s):
        if char == '(':
            stack.append(char)
            tmp *= 2
        elif char == '[':
            stack.append(char)
            tmp *= 3
        elif char == ')':
            if not stack or stack[-1] != '(':
                return 0
            if s[i - 1] == '(':
                total += tmp
                
            stack.pop()
            tmp //= 2
        elif char == ']':
            if not stack or stack[-1] != '[':
                return 0
            if s[i - 1] == '[':
                total += tmp
            stack.pop()
            tmp //= 3
    return total if not stack else 0
print(sol(s=s))