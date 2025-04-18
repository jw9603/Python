# 백준 10828. 스택
# https://www.acmicpc.net/problem/10828
import sys
N = int(sys.stdin.readline().strip())
stack = []
for _ in range(N):
    command = sys.stdin.readline().split()

    if command[0] == 'push':
        stack.append(int(command[1]))
    elif command[0] == 'pop':
        print(-1 if not stack else stack.pop())
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        print(0 if stack else 1)
    else:
        print(-1 if not stack else stack[-1])
        
        