# 백준 28278. 스택 2
# https://www.acmicpc.net/problem/28278
import sys
N = int(sys.stdin.readline().strip())
stack = []
for _ in range(N):
    command = sys.stdin.readline().split()
    if command[0] == '1':
        stack.append(int(command[1]))
    elif command[0] == '2':
        print(stack.pop() if stack else -1)
    elif command[0] == '3':
        print(len(stack))
    elif command[0] == '4':
        print(1 if not stack else 0)
    else:
        print(stack[-1] if stack else -1)