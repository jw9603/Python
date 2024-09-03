class Node:
    
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None
        

class LinkedList:
    '''해시 테이블에서 충돌을 처리하기 위한 링크드 리스트'''
    
    def __init__(self):
        self.head = None
        
    def insert(self,key,value):
        
        if not self.head:
            self.head = Node(key,value)
        
        else: # if self.head
            current = self.head
            while current:
                if current.key == key:
                    current.value = value
                    return
                if not current.next:
                    break
                current = current.next
            current.next = Node(key,value)
    
    def search(self,key):
        current = self.head
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None
    
    def delete(self,key):
        current = self.head
        # 현재 링크드 리스트: 1->2->3
        # 3을 삭제하고 싶어
        # current = 1
        # prev = None
        prev = None
        while current: 
            if current.key == key: # current가 삭제하고 싶은 키일때
                if prev:
                    prev.next = current.next
                else: # None
                    self.head = current.next
            prev = current    
            current = current.next
    
    def __str__(self):
        
        nodes = []
        current = self.head 
        
        while current:
            nodes.append(f"({current.key}: {current.value})")
            current = current.next
        return ' -> '.join(nodes)            
                         
        
    
