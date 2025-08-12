class Node:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def insert(self, value, idx=None):
        new_node = Node(value)

        # idx가 None이거나, 현재 리스트의 끝이면 마지막에 삽입
        if idx is None or idx >= self.size:
            # head가 없다면?
            if self.head is None:
                self.head = new_node
                self.tail = new_node
            else:
                self.tail.next = new_node
                new_node.prev = self.tail
                self.tail = new_node
        
        # 첫 번째 index인 경우
        elif idx == 0:
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node

            # 추가 되어서 노드가 1개라면
            if self.size == 0:
                self.tail = new_node
        
        # 중간 위치에 삽입
        else:
            current = self.head
            for _ in range(idx - 1):
                current = current.next
            
            new_node.next = current.next
            new_node.prev = current

            if current.next:
                current.next.prev = new_node
            
            current.next = new_node
        
        self.size += 1
    
    def remove(self, idx=None):
        if self.head is None:
            return
        
        # idx가 None이거나 리스트의 끝이면 마지막 요소 삭제
        if idx is None:
            idx = self.size - 1
        
        if idx < 0 or idx >= self.size:
            raise IndexError('Index out of bounds')

        # 첫 번째 값 삭제
        if idx == 0:
            # 노드가 1개인 경우
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
        
        # 맨 끝
        elif idx == self.size - 1:
            # 노드가 1개인 경우
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.tail = self.tail.prev
                self.tail.next = None
        
        # 중간 위치에 삽입
        else:
            current = self.head
            for _ in range(idx - 1):
                current = current.next
            
            remove_node = current.next
            current.next = remove_node.next

            if remove_node.next:
                remove_node.next.prev = current
        
        self.size -= 1
    
    def get(self, idx):
        if idx < 0 or idx >= self.size:
            raise IndexError('Index out of bounds')

        # 중간 지점을 기준으로 head or tail에서 탐색 시작
        if idx < self.size // 2:
            current = self.head
            for _ in range(idx):
                current = current.next
        
        else:
            current = self.tail
            for _ in range(self.size - idx - 1):
                current = current.prev
        
        return current.value

    def print_linked_list(self):
        current = self.head

        while current.next:
            print(current.value, end = ' <-> ')
            current = current.next

        print(current.value)            

if __name__ == '__main__':
    dll = DoublyLinkedList()

    # 요소 추가
    for i in range(5):
        dll.insert(i)
    dll.print_linked_list()

    # 첫 번째 위치에 추가
    dll.insert(10, 0)
    dll.print_linked_list()

    # 중간 위치에 추가
    dll.insert(20, 3)
    dll.print_linked_list()

    # 요소 삭제
    dll.remove()  # 마지막 요소 삭제
    dll.print_linked_list()

    dll.remove(0)  # 첫 번째 요소 삭제
    dll.print_linked_list()

    dll.remove(2)  # 중간 요소 삭제
    dll.print_linked_list()


    print(dll.get(3))