# 1406. 에디터
# https://www.acmicpc.net/problem/1406
import sys

s = list(sys.stdin.readline().strip())
M = int(sys.stdin.readline().strip())

cursor_right = []
for _ in range(M):
    order = sys.stdin.readline().split()
    
    if order[0] == 'L':
        if s:
            cursor_right.append(s.pop())
    elif order[0] == 'D':
        if cursor_right:
            s.append(cursor_right.pop())
    elif order[0] == 'B':
        if s:
            s.pop()
    else:
        s.append(order[1])

s.extend(cursor_right[::-1])
print(''.join(s))