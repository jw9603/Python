# 1472. Design Browser History
# https://leetcode.com/problems/design-browser-history/description/

class Node:
    def __init__(self,val=0,next=None,prev=None):
        self.val = val
        self.next = next
        self.prev = prev
# Linked List 풀이
class BrowserHistory(object):
    
    # 1. Linked List
    def __init__(self, homepage):
        """
        :type homepage: str
        """
        self.current = Node(homepage)
        
    
    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        self.current.next = Node(val=url)
        self.current = self.current.next
        return None
    
    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        while steps > 0 and self.current.prev != None:
            steps -= 1
            self.current = self.current.prev
        return self.current.val
    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        while steps > 0 and self.current.next != None:
            steps -= 1
            self.current = self.current.next
        return self.current.val
    
    # 2. Array
    def __init__(self, homepage):
        """
        :type homepage: str
        """
        self.list = [homepage]
        self.idx = 0
        
        
    
    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        while self.idx != len(self.list) - 1:
            self.list.pop()
        self.list.append(url)
        self.idx += 1
        
       
    
    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        if self.idx < steps:
            self.idx = 0
        else:
            self.idx -= steps
        
        return self.list[self.idx]
   
    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        if self.idx + steps > len(self.list) - 1:
            self.idx = len(self.list) - 1
        else:
            self.idx += steps
        return self.list[self.idx]
    
    # 3. Stack
    def __init__(self, homepage):
        """
        :type homepage: str
        """
        self.current = homepage
        self.back_stack = []
        self.forward_stack = []

        
    
    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        self.back_stack.append(url)
        self.current = url
        self.forward_stack = []

    
    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        while steps > 0 and self.back_stack:
            self.forward_stack.append(self.current)
            
            self.current  = self.back_stack.pop()
            steps -= 1
        return self.current
   
    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        while steps > 0 and self.forward_stack:
            self.back_stack.append(self.current)
            
            self.current = self.forward_stack.pop()
            steps -= 1
        return self.current
 