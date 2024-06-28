'''
정수를 저장하는 덱을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

명령은 총 여덟 가지이다.

1 X: 정수 X를 덱의 앞에 넣는다. (1 ≤ X ≤ 100,000)
2 X: 정수 X를 덱의 뒤에 넣는다. (1 ≤ X ≤ 100,000)
3: 덱에 정수가 있다면 맨 앞의 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다.
4: 덱에 정수가 있다면 맨 뒤의 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다.
5: 덱에 들어있는 정수의 개수를 출력한다.
6: 덱이 비어있으면 1, 아니면 0을 출력한다.
7: 덱에 정수가 있다면 맨 앞의 정수를 출력한다. 없다면 -1을 대신 출력한다.
8: 덱에 정수가 있다면 맨 뒤의 정수를 출력한다. 없다면 -1을 대신 출력한다.
'''
import sys
from collections import deque
N = int(sys.stdin.readline().strip())
deque = deque()
for _ in range(N):
    data = sys.stdin.readline().split()
    
    if data[0] == '1': # 1 X: 정수 X를 덱의 앞에 넣는다. (1 ≤ X ≤ 100,000)
        deque.appendleft(data[1])
    elif data[0] == '2': # 2 X: 정수 X를 덱의 뒤에 넣는다. (1 ≤ X ≤ 100,000)
        deque.append(data[1])
    elif data[0] == '3': # 3: 덱에 정수가 있다면 맨 앞의 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다.
        if deque:
            print(deque.popleft())
            continue
        print(-1)
    elif data[0] == '4': # 4: 덱에 정수가 있다면 맨 뒤의 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다.
        if deque:
            print(deque.pop())
            continue
        print(-1)
    elif data[0] == '5': # 5: 덱에 들어있는 정수의 개수를 출력한다.
        print(len(deque))
    elif data[0] == '6': # 6: 덱이 비어있으면 1, 아니면 0을 출력한다.
        if deque:
            print(0)
            continue
        print(1)
    elif data[0] == '7': # 7: 덱에 정수가 있다면 맨 앞의 정수를 출력한다. 없다면 -1을 대신 출력한다.
        if deque:
            print(deque[0])
            continue
        print(-1)
    elif data[0] == '8': # 8: 덱에 정수가 있다면 맨 뒤의 정수를 출력한다. 없다면 -1을 대신 출력한다.
        if deque:
            print(deque[len(deque)-1])
            continue
        print(-1)
    
        
        