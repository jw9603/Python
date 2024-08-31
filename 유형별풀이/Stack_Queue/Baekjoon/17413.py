# 17413 단어 뒤집기 2
# https://www.acmicpc.net/problem/17413
import sys
from collections import deque

S = sys.stdin.readline().strip()

stack = deque()
result = ''
tag = False

for i in S:
    if i == '<':
        while stack:
            result += stack.pop()
        tag=True
        result += i
    elif i == '>':
        tag=False
        result += i
    elif tag:
        result += i
    elif i == ' ':
        while stack:
            result += stack.pop()
        result+=i
    else:
        stack.append(i)
        
while stack:
    result += stack.pop()
    
print(result)
