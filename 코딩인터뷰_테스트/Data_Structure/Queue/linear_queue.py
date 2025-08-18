class LinearQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    def is_empty(self):
        return self.front == self.rear

    def is_full(self):
        return self.rear == self.size - 1
    
    def enqueue(self, value):
        if self.is_full():
            raise OverflowError('Queue is Full!')

        self.rear += 1
        self.queue[self.rear] = value
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from empty queue!")
        
        self.front += 1
        value = self.queue[self.front]
        self.queue[self.front] = None

        return value

    def top(self):
        if self.is_empty():
            raise IndexError('Peek from empty queue!')
        
        return self.queue[self.front + 1]

    def __str__(self):
        return f"Queue({self.queue}, front={self.front}, rear={self.rear})"

if __name__ == '__main__':
    q = LinearQueue(5)

    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)

    print(q)                             # Queue([10, 20, 30, None, None], front=-1, rear=2)

    print(f"Front element: {q.top()}")   # Front element: 10

    print(f"Dequeue: {q.dequeue()}")     # Dequeue: 10
    print(q)                             # Queue([None, 20, 30, None, None], front=0, rear=2)

    q.enqueue(40)                        
    q.enqueue(50)                        
    print(q)                             # Queue([None, 20, 30, 40, 50], front=0, rear=4)