from collections import deque

class Stack:

    def __init__(self):
        self.items = deque() # [] 대신 deque(), deque([])처럼 해도 됨

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError('You popped from an empty stack')

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("You peeked from an empty stack")

    def size(self):
        return len(self.items)

    def __repr__(self):
        return f"Stack({list(self.items)})"

    def __str__(self):
        return str(list(self.items))
    

if __name__ == '__main__':
    
    # 스택 생성
    stack = Stack()

    # 스택에 요소 추가
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(f"스택 상태: {stack}")

    # 스택에서 요소 제거
    print(f"pop: {stack.pop()}")
    print(f"스택 상태: {stack}")

    # 스택의 맨 위 요소 확인
    print(f"peek: {stack.peek()}")
    print(f"스택 상태: {stack}")

    # 스택의 크기 확인
    print(f"스택 크기: {stack.size()}")

    # 스택 비어 있는지 확인
    print(f"스택이 비어 있는가? {stack.is_empty()}")