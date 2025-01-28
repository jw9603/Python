# 백준 10773. 제로
# https://www.acmicpc.net/problem/10773
import sys
K = int(sys.stdin.readline().strip())
stack = []
for _ in range(K):
    num = int(sys.stdin.readline().strip())
    if num != 0:
        stack.append(num)
    else:
        stack.pop()
print(sum(stack))