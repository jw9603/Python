class Node:
    def __init__(self,data):
        self.data = data # 노드가 저장하는 데이터
        self.next = None # 다음 노드를 가리키는 포인터
        

class LinkedList:
    def __init__(self,data):
        self.head = Node(data) # 링크드 리스트의 첫번째 데이터
        
    def append(self,data):
        if self.head is None:
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)
            
    
    def print_linked_list(self):
        current = self.head
        while current:
            print(current.data,end=' -> ')
            current = current.next
        print('None')
        
    def delete(self,data):
        
        if self.head == '':
            print('This data is not in our linked list')
            return

        if self.head.data == data:
            tmp = self.head
            self.head = self.head.next
            tmp = None
        else:
            current = self.head
            while current.next:
                if current.next.data == data:
                    tmp = current.next
                    current.next = current.next.next
                    tmp = None
                    return
                else:
                    current = current.next
                    
    def insert_before(self,target_data,data): # target_data 앞에 data를 삽입하는 메서드
        
        if self.head is None:
            print('Linked List is empty')
            return
        
        if self.head.data == target_data:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            return
        
        current = self.head
        while current.next and current.next.data != target_data:
            current = current.next
        
        if current.next is None:
            print(f"Node with data {target_data} not found.")
        
        else: # current.next가 target_data일 때
            new_node = Node(data)
            new_node.next = current.next
            current.next = new_node
            
    def insert_after(self,target_data,data): # target_data 뒤에 data를 삽입하는 메서드
        
        if self.head is None:
            print('Linked List is empty')
            return

        current = self.head
        
        while current is not None:
            if current.data == target_data:
                
                new_node = Node(data)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
        
        # target_data를 찾지 못한 경우
        print(f'Node with data {target_data} not found.')

        
            

# 링크드 리스트 사용 예제
if __name__ == '__main__':
    
    ll = LinkedList(0)
    
    # 1부터 11 넣기
    for i in range(1,11):
        ll.append(i)
    
    # 결과 출력
    ll.print_linked_list() # 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10 -> None
    
    ll.delete(5)
    
    ll.print_linked_list() # 0 -> 1 -> 2 -> 3 -> 4 -> 6 -> 7 -> 8 -> 9 -> 10 -> None
    
    # 5 앞에 99 삽입
    ll.insert_before(5, 99) # Node with data 5 not found.
    
    ll.print_linked_list()  # 0 -> 1 -> 2 -> 3 -> 4 -> 6 -> 7 -> 8 -> 9 -> 10 -> None
    
    # 6 앞에 99 삽입
    ll.insert_before(6, 99)
    
    ll.print_linked_list() # 0 -> 1 -> 2 -> 3 -> 4 -> 99 -> 6 -> 7 -> 8 -> 9 -> 10 -> None
    
    
    # 0 뒤에 15 삽입 (헤드 노드 뒤에 삽입하는 경우)
    ll.insert_after(0, 15)
    
    ll.print_linked_list() # 0 -> 15 -> 1 -> 2 -> 3 -> 4 -> 99 -> 6 -> 7 -> 8 -> 9 -> 10 -> None
    
    # 8 뒤에 77 삽입
    ll.insert_after(8,77)
    
    ll.print_linked_list() # 0 -> 15 -> 1 -> 2 -> 3 -> 4 -> 99 -> 6 -> 7 -> 8 -> 77 -> 9 -> 10 -> None