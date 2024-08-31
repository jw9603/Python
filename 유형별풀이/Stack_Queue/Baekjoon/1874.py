# 스택 수열2 1874번
# https://www.acmicpc.net/problem/1874

import sys

n = int(sys.stdin.readline().strip())

stack = [1]
start = 2
ans = ['+']
flag = True
for _ in range(n):
    num = int(sys.stdin.readline().strip())
    
    while start <= num:
        stack.append(start)
        ans.append('+')
        start += 1
    
    if stack[-1] == num:
        stack.pop()
        ans.append('-')
    else:
        flag = False
        
print('\n'.join(ans) if flag else 'NO')

    
