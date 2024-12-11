# 10773. 제로
# https://www.acmicpc.net/problem/10773

import sys
k = int(sys.stdin.readline().strip())
stack = []
for _ in range(k):
    data = int(sys.stdin.readline().strip())
    if data == 0:
        stack.pop()
        continue
    stack.append(data)
print(sum(stack))