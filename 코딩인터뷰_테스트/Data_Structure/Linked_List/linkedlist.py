class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.size = 0
    
    def insert(self, value, idx=None):
        new_node = Node(value)

        # idx가 None이거나 idx가 리스트 끝이라면 마지막에 삽입
        if idx is None or idx >= self.size:
            # Head가 None이라면, new node가 head
            if self.head is None:
                self.head = new_node
            else:
                current = self.head
                while current.next:
                    current = current.next
                current.next = new_node
        
        # 첫 번째 index인 경우
        elif idx == 0:
            new_node.next = self.head
            self.head = new_node

        # 중간에 삽입
        else:
            current = self.head
            for _ in range(idx - 1):
                current = current.next
            
            new_node.next = current.next
            current.next = new_node
        
        self.size += 1
    
    def remove(self, idx=None):
        if self.head is None:
            return
        
        # 인덱스가 주어지지 않은 경우, 마지막 요소 삭제
        if idx is None:
            idx = self.size - 1
        
        if idx < 0 or idx >= self.size:
            raise IndexError('Index out of bounds')

        # 첫 번째 요소 제거
        if idx == 0:
            self.head = self.head.next
        
        # 중간 위치의 값 제거
        else:
            current = self.head
            for _ in range(idx - 1):
                current = current.next
            current.next = current.next.next
        
        self.size -= 1
    
    def get(self, idx):
        if idx < 0 or idx >= self.size:
            raise IndexError('Index out of bounds')

        current = self.head
        
        for _ in range(idx):
            current = current.next
        
        return current.value
    
    def print_linked_list(self):
        current = self.head

        while current.next:
            print(current.value, end=' -> ')
            current = current.next
        print(current.value)
    
if __name__ == '__main__':
    ll = LinkedList()

    for i in range(0, 11):
        ll.insert(i)
    
    ll.print_linked_list() # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

    ll.get(2)              # 2

    ll.remove(4)           

    ll.print_linked_list() # 0, 1, 2, 3, 5, 6, 7, 8, 9, 10