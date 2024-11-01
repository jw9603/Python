# 1472. Design Browser History
# https://leetcode.com/problems/design-browser-history/description/

####################### 1. Linked List 풀이 ####################### 

class Node:
    def __init__(self,val=0,next=None,prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class BrowserHistory(object):
    
    def __init__(self,homepage):
        
        self.current = Node(val=homepage)
        
    def visit(self,url): # O(1)
        """
        :type url: str
        :rtype: None
        """
        
        self.current.next = Node(val=url,prev=self.current)
        self.current = self.current.next
        return None
    
    def back(self,steps): # Time Complexity: O(min(steps, d)) -> O(n), where d is the distance to the first page.
        """
        :type steps: int
        :rtype: str
        """
        while steps > 0 and self.current.prev != None:
            steps -= 1
            self.current = self.current.prev
        return self.current.val
    
    def forward(self,steps): # Time Complexity: O(min(steps, d)) -> O(n), where d is the distance to the end page.
        """
        :type steps: int
        "rtype: str
        """
        while steps > 0 and self.current.next != None:
            steps -= 1
            self.current = self.current.next
        return self.current.val
    
####################### 1. Linked List 풀이 ####################### 


####################### 2. Array List 풀이 ####################### 
class BrowserHistory(object):
    def __init__(self,homepage):
        
        self.list = [homepage]
        self.current_idx = 0
    
    def visit(self,url): # O(n)
        """
        :type url: str
        :rtype: None
        """
        while self.current_idx != len(self.list) - 1:
            self.list.pop()
        
        self.list.append(url)
        self.current_idx += 1
        
        return None
    
    def back(self,steps): # O(1)
        """ 
        :type steps: int
        :rtype: str
        """
        if self.current_idx < steps:
            self.current_idx = 0
        else:
            self.current_idx -= steps
        
        return self.list[self.current_idx]
    
    def forward(self,steps): # O(1)
        """
        :type steps: int
        "rtype: str
        """
        if self.current_idx + steps > len(self.list) - 1:
            self.current_idx = len(self.list) - 1
        else:
            self.current_idx += steps
        
        return self.list[self.current_idx]
    
####################### 2. Array List 풀이 ####################### 

######################### 3. Stack 풀이 ######################### 
class BrowserHistory(object):
    def __init__(self,homepage):
        self.current = homepage
        self.back_stack = []
        self.forward_stack = []
        
    def visit(self,url): # O(1)
        """
        :type url: str
        :rtype: None
        """
        self.back_stack.append(self.current)
        
        self.current = url
        
        self.forward_stack.clear()
        
    def back(self,steps): # O(steps)
        
        while steps > 0 and self.back_stack:
            self.forward_stack.append(self.current)
            
            self.current = self.back_stack.pop()
            steps -= 1
            
        return self.current
     
    def forward(self,steps): # O(steps)
        
        while steps > 0 and self.forward_stack:
            self.back_stack.append(self.current)
            
            self.current = self.forward_stack.pop()
            steps -= 1
        
        return self.current
    
######################### 3. Stack 풀이 ######################### 
    

if __name__ == '__main__':
    

    obj = BrowserHistory("leetcode.com")
    print(obj.visit('google.com'))          # None
    print(obj.visit('facebook.com'))        # None
    print(obj.visit('youtube.com'))         # None
    print(obj.back(1))                      # facebook.com
    print(obj.back(1))                      # google.com
    print(obj.forward(1))                   # facebook.com
    
    print(obj.visit('linkedin.com'))        # None
    print(obj.forward(2))                   # linkedlin.com
    print(obj.back(2))                      # google.com
    print(obj.back(7))                      # leetcode.com