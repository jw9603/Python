from collections import deque
import time

class Queue_list:
    
    def __init__(self):
        self.items = []
        
    def is_empty(self):
        return len(self.items) == 0
    
    def enqueue(self,item):
        self.items.append(item)
    
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError('You dequeued from an empty queue')
    
    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError('You peeked from an empty queue')
    
    def size(self):
        return len(self.items)
    
    def __repr__(self):
        return f"Queue({self.items})"

    def __str__(self):
        return str(self.items)
    
class Queue:
    
    def __init__(self):
        self.items = deque()
        
    def is_empty(self):
        return len(self.items) == 0
    
    def enqueue(self,item):
        self.items.append(item)
    
    def dequeue(self):
        if not self.is_empty():
            return self.items.popleft()
        else:
            raise IndexError('You dequeued from an empty queue')
    
    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("You peeked from an empty queue")
    
    def size(self):
        return len(self.items)
    
    def __repr__(self):
        return f"Queue({self.items})"
    
    def __str__(self):
        return str(self.items)
    
    
if __name__ == '__main__':
    
    
    
    a = time.time()
    Queue_list = Queue_list()

    # 큐에 요소 추가
    Queue_list.enqueue(1)
    Queue_list.enqueue(2)
    Queue_list.enqueue(3)
    print(f"큐 상태: {Queue_list}")

    # 큐에서 요소 제거
    print(f"dequeue: {Queue_list.dequeue()}")
    print(f"큐 상태: {Queue_list}")

    # 큐의 맨 앞 요소 확인
    print(f"peek: {Queue_list.peek()}")
    print(f"큐 상태: {Queue_list}")

    # 큐의 크기 확인
    print(f"큐 크기: {Queue_list.size()}")

    # 큐 비어 있는지 확인
    print(f"큐가 비어 있는가? {Queue_list.is_empty()}")
    
    print(f"{time.time()-a:.6f}")
    
    
    print('\n')
    
    a1 = time.time()
    queue = Queue()

    # 큐에 요소 추가
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(f"큐 상태: {queue}")

    # 큐에서 요소 제거
    print(f"dequeue: {queue.dequeue()}")
    print(f"큐 상태: {queue}")

    # 큐의 맨 앞 요소 확인
    print(f"peek: {queue.peek()}")
    print(f"큐 상태: {queue}")

    # 큐의 크기 확인
    print(f"큐 크기: {queue.size()}")

    # 큐 비어 있는지 확인
    print(f"큐가 비어 있는가? {queue.is_empty()}")
    
    print(f"{time.time()-a1:.6f}")