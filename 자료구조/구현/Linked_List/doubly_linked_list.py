class Node:
    def __init__(self, data):
        self.data = data  # 노드가 저장하는 데이터
        self.next = None  # 다음 노드를 가리키는 포인터
        self.prev = None  # 이전 노드를 가리키는 포인터

class DoublyLinkedList:
    def __init__(self, data):
        self.head = Node(data)  # 리스트의 첫 번째 노드

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            new_node = Node(data)
            node.next = new_node
            new_node.prev = node  # 새 노드의 prev를 마지막 노드로 설정

    def print_linked_list(self):
        current = self.head
        while current:
            print(current.data, end=' <-> ')
            current = current.next
        print('None')

    def delete(self, data):
        if self.head is None:
            print('This data is not in our linked list')
            return

        if self.head.data == data:
            tmp = self.head
            self.head = self.head.next
            if self.head:
                self.head.prev = None  # 헤드 노드의 prev를 None으로 설정
            tmp = None
        else:
            current = self.head
            while current.next:
                if current.next.data == data:
                    tmp = current.next
                    current.next = current.next.next
                    if current.next:
                        current.next.prev = current  # 삭제된 노드의 다음 노드의 prev를 현재 노드로 설정
                    tmp = None
                    return
                else:
                    current = current.next

    def insert_before(self, target_data, data):
        if self.head is None:
            print('Linked List is empty')
            return

        if self.head.data == target_data:
            new_node = Node(data)
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            return

        current = self.head
        while current.next and current.next.data != target_data:
            current = current.next

        if current.next is None:
            print(f"Node with data {target_data} not found.")
        else:
            new_node = Node(data)
            new_node.next = current.next
            new_node.prev = current
            current.next.prev = new_node
            current.next = new_node

    def insert_after(self, target_data, data):
        if self.head is None:
            print('Linked List is empty')
            return

        current = self.head

        while current is not None:
            if current.data == target_data:
                new_node = Node(data)
                new_node.next = current.next
                new_node.prev = current
                if current.next:
                    current.next.prev = new_node
                current.next = new_node
                return
            current = current.next

        print(f'Node with data {target_data} not found.')

# 이중 연결 리스트 사용 예제
if __name__ == '__main__':

    dll = DoublyLinkedList(0)

    # 1부터 10까지 데이터를 삽입
    for i in range(1, 11):
        dll.append(i)

    # 리스트 출력
    dll.print_linked_list()  # 0 <-> 1 <-> 2 <-> 3 <-> 4 <-> 5 <-> 6 <-> 7 <-> 8 <-> 9 <-> 10 <-> None

    # 특정 노드 삭제
    dll.delete(5)
    dll.print_linked_list()  # 0 <-> 1 <-> 2 <-> 3 <-> 4 <-> 6 <-> 7 <-> 8 <-> 9 <-> 10 <-> None

    # 특정 노드 앞에 데이터 삽입
    dll.insert_before(4, 99)
    dll.print_linked_list()  # 0 <-> 1 <-> 2 <-> 3 <-> 99 <-> 4 <-> 6 <-> 7 <-> 8 <-> 9 <-> 10 <-> None

    # 특정 노드 뒤에 데이터 삽입
    dll.insert_after(7, 77)
    dll.print_linked_list()  # 0 <-> 1 <-> 2 <-> 3 <-> 99 <-> 4 <-> 6 <-> 7 <-> 77 <-> 8 <-> 9 <-> 10 <-> None


            