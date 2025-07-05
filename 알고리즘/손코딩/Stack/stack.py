# 스택 두 개로 큐 구현하기
class Queue:
    def __init__(self):
        self.in_stack = []  # 데이터를 삽입할 떄
        self.out_stack = [] # 데이터를 뺄 때

    def enqueue(self, x):
        self.in_stack.append(x)
    
    def dequeue(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        
        if not self.out_stack:
            return None
        return self.out_stack.pop()

# 큐 두 개로 스택 구현하기
from collections import deque
class Stack:
    def __init__(self):
        # q1은 항상 최종적으로 pop할 요소가 뒤에 오도록 유지
        # push시에 q2에 삽입하고 q1의 요소를 모두 이동
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x):
        self.q2.append(x)

        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1
        
    def pop(self):
        if not self.q1:
            return None
        return self.q1.popleft()

if __name__ == '__main__':
    print("STACK")
    s = Stack()
    s.push(1)
    s.push(2)
    print(s.pop())
    s.push(3)
    print(s.pop())
    print("QUEUE")
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    print(q.dequeue())
    q.enqueue(3)
    print(q.dequeue())