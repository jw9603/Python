class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = 0
        self.rear = 0
        self.count = 0
    
    def is_empty(self):
        return self.count == 0
    
    def is_full(self):
        return self.count == self.size
    
    def enqueue(self, value):
        if self.is_full():
            raise OverflowError('Queue is full!')
        
        self.queue[self.rear] = value
        self.rear = (self.rear + 1) % self.size
        self.count += 1
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from empty queue!")

        value = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.size
        self.count -= 1

        return value

    def top(self):
        if self.is_empty():
            raise IndexError("Peek from empty queue!")
        
        return self.queue[self.front]
    
    def __str__(self):
        return f"Circular Queue={self.queue}, front={self.front}, rear={self.rear}, count={self.count}"

if __name__ == "__main__":
    cq = CircularQueue(5)

    cq.enqueue(10)
    cq.enqueue(20)
    cq.enqueue(30)
    print(cq)  # Circular Queue=[10, 20, 30, None, None], front=0, rear=3, count=3

    print("Dequeue:", cq.dequeue())  # 10
    print(cq)  # Circulqr Queue=[None, 20, 30, None, None], front=1, rear=3, count=2

    cq.enqueue(40)
    print(cq)  # Circular Queue=[None, 20, 30, 40, None], front=1, rear=4, count=3
    cq.enqueue(50) 
    print(cq)  # Circular Queue=[None, 20, 30, 40, 50], front=1, rear=0, count=4
    cq.enqueue(60)
    print(cq)  # 꽉 찬 상태 (count=5), Circular Queue=[60, 20, 30, 40, 50], front=1, rear=1, count=5

    # cq.enqueue(70) 하면 OverflowError 발생