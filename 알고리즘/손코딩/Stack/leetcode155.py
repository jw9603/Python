# LeetCode 155. Min Stack
# https://leetcode.com/problems/min-stack/
class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
        
    def pop(self):
        """
        :rtype: None
        """
        if self.stack:
            val = self.stack.pop()
            
            if val == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1] if self.stack else None
    
    def getMin(self):
        """
        :rtype: int
        """
        return self.min_stack[-1] if self.min_stack else None