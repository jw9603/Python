# 1406 에디터
# https://www.acmicpc.net/problem/1406

################## 덱을 활용한 풀이 #######################
import sys
from collections import deque

s1 = deque(sys.stdin.readline().strip()) # 이 문자열의 길이 N
M = int(sys.stdin.readline().strip())

s2 = deque() # 커서를 기준으로 오른쪽


for _ in range(M):
    order = sys.stdin.readline().split()
    
    if order[0] == 'L':
        if s1:
            s2.appendleft(s1.pop())
    elif order[0] == 'D':
        if s2:
            s1.append(s2.popleft())
    elif order[0] == 'B':
        if s1:
            s1.pop()
    else:
        s1.append(order[1])

s1.extend(s2)

print(''.join(s1))
################## 덱을 활용한 풀이 #######################



################## 스택을 활용한 풀이 #######################
import sys


s1 = list(sys.stdin.readline().strip()) # 이 문자열의 길이 N
M = int(sys.stdin.readline().strip())

s2 = list() # 커서를 기준으로 오른쪽


for _ in range(M):
    order = sys.stdin.readline().split()
    
    if order[0] == 'L':
        if s1:
            s2.append(s1.pop())
    elif order[0] == 'D':
        if s2:
            s1.append(s2.pop())
    elif order[0] == 'B':
        if s1:
            s1.pop()
    else:
        s1.append(order[1])

s1.extend(s2[::-1])

print(''.join(s1))
################## 스택을 활용한 풀이 #######################
