import sys
from collections import deque

N = int(sys.stdin.readline().strip())
stack = deque()
for _ in range(N):
    command = sys.stdin.readline().split()
   
    if command[0] == 'push':
        stack.append(int(command[1]))
    elif command[0] == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        print(int(len(stack)==0))
    elif command[0] == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)
  
    