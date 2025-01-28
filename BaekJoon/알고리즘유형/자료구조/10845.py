# 백준 10845. 큐
# https://www.acmicpc.net/problem/10845
import sys

N = int(sys.stdin.readline().strip())
queue = []
for _ in range(N):
    command = sys.stdin.readline().split()

    if command[0] == 'push':
        queue.append(int(command[1]))
    elif command[0] == 'pop':
        print(-1 if not queue else queue.pop(0))
    elif command[0] == 'size':
        print(len(queue))
    elif command[0] == 'empty':
        print(0 if queue else 1)
    elif command[0] == 'front':
        print(queue[0] if queue else -1)
    else:
        print(queue[-1] if queue else -1)