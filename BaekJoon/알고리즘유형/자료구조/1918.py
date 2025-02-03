# 백준 1918. 후위 표기식
# https://www.acmicpc.net/problem/1918
import sys
s = sys.stdin.readline().strip()

def sol(s):
    result = []
    stack = []
    priority = {'+':1, '-':1, '*':2, '/':2, '(':0}
    
    for char in s:
        if char.isalpha():
            result.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()
        else:
            while stack and priority[stack[-1]] >= priority[char]:
                result.append(stack.pop())
            stack.append(char)
    while stack:
        result.append(stack.pop())
    return result
print(*sol(s=s), sep='')
    
    