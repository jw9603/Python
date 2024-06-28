'''
정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

명령은 총 다섯 가지이다.

1 X: 정수 X를 스택에 넣는다. (1 ≤ X ≤ 100,000)
2: 스택에 정수가 있다면 맨 위의 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다.
3: 스택에 들어있는 정수의 개수를 출력한다.
4: 스택이 비어있으면 1, 아니면 0을 출력한다.
5: 스택에 정수가 있다면 맨 위의 정수를 출력한다. 없다면 -1을 대신 출력한다.

'''

import sys

a = int(sys.stdin.readline())
stack_list = []
input_order = []
for _ in range(a):
    order_data = sys.stdin.readline().split()
    if order_data[0]=='1':  # 1 X: 정수 X를 스택에 넣는다. (1 ≤ X ≤ 100,000)
        stack_list.append(int(order_data[-1]))
    elif order_data[0] == '2': # 2: 스택에 정수가 있다면 맨 위의 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다.
        if stack_list:
            print(stack_list.pop())
            continue
        print(-1)
    elif order_data[0] == '3': # 3: 스택에 들어있는 정수의 개수를 출력한다.
        print(len(stack_list))
    elif order_data[0] == '4': # 4: 스택이 비어있으면 1, 아니면 0을 출력한다.
        if len(stack_list) == 0:
            print(1)
        else:
            print(0)
    elif order_data[0] == '5':
        if len(stack_list)!=0:
            print(stack_list[-1])
        else:
            print(-1)
            

        
    