# LeetCode 1472. Design Browser History
# https://leetcode.com/problems/design-browser-history/
class Node:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class BrowserHistory(object):

    def __init__(self, homepage):
        """
        :type homepage: str
        Initializes the object with the homepage of the browser.
        """
        self.current = Node(homepage)
        
    def visit(self, url):
        """
        :type url: str
        :rtype: None
        Visits url from the current page. It clears up all the forward history.
        """
        self.current.next = Node(val=url, prev=self.current)
        self.current = self.current.next
        
        return None
        
    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        Move steps back in history. 
        If you can only return x steps in the history and steps > x, you will return only x steps.
        Return the current url after moving back in history at most steps.
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
    
# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)

# 1. leetcode -> google -> facebook -> youtube           
