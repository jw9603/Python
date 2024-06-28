'''
정수를 저장하는 큐를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

명령은 총 여섯 가지이다.

push X: 정수 X를 큐에 넣는 연산이다.
pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 큐에 들어있는 정수의 개수를 출력한다.
empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.

'''
##### 아래 코드는 시간 초과가 발생한다 ####
# import sys
# N = int(sys.stdin.readline().strip())

# queue = [] # FIFO
# for _ in range(N):
#     data = sys.stdin.readline().split()
    
#     if data[0] == 'push': # push X: 정수 X를 큐에 넣는 연산이다.
#         queue.append(int(data[-1]))
#     elif data[0] == 'pop': # pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
#         if queue:
#             print(queue.pop(0))
#             continue
#         print(-1)
#     elif data[0] == 'size':  # size: 큐에 들어있는 정수의 개수를 출력한다.
#         print(len(queue))
#     elif data[0] == 'empty': # empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
#         if queue:
#             print(0)
#             continue
#         print(1)
#     elif data[0] == 'front': # front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
#         if queue:
#             print(queue[0])
#             continue
#         print(-1)
#     elif data[0] == 'back': # back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
#         if queue:
#             print(queue[-1])
#             continue
#         print(-1)
#######################################################################################
import sys
from collections import deque
N = int(sys.stdin.readline().strip())

queue = deque([]) # FIFO
for _ in range(N):
    data = sys.stdin.readline().split()
    
    if data[0] == 'push': # push X: 정수 X를 큐에 넣는 연산이다.
        queue.append(int(data[1]))
    elif data[0] == 'pop': # pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
        if queue:
            print(queue.popleft())
            continue
        print(-1)
    elif data[0] == 'size':  # size: 큐에 들어있는 정수의 개수를 출력한다.
        print(len(queue))
    elif data[0] == 'empty': # empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
        if queue:
            print(0)
            continue
        print(1)
    elif data[0] == 'front': # front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
        if queue:
            print(queue[0])
            continue
        print(-1)
    elif data[0] == 'back': # back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
        if queue:
            print(queue[-1])
            continue
        print(-1)

    