# 백준 10866. 덱
# https://www.acmicpc.net/problem/10866
import sys
from collections import deque
N = int(sys.stdin.readline().strip())
deque = deque()
for _ in range(N):
    command = sys.stdin.readline().split()
    
    if command[0] == 'push_front':
        deque.appendleft(int(command[1]))
    elif command[0] == 'push_back':
        deque.append(int(command[1]))
    elif command[0] == 'pop_front':
        print(deque.popleft() if deque else -1)
    elif command[0] == 'pop_back':
        print(deque.pop() if deque else -1)
    elif command[0] == 'size':
        print(len(deque))
    elif command[0] == 'empty':
        print(0 if deque else 1)
    elif command[0] == 'front':
        print(deque[0] if deque else -1)
    else: # back
        print(deque[-1] if deque else -1)
        