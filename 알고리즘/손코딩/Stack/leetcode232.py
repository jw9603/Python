# LeetCode 232. Implement Queue using Stacks
# https://leetcode.com/problems/implement-queue-using-stacks/description/

class MyQueue(object):

    def __init__(self):
        self.in_stack = []
        self.out_stack = []
    
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.in_stack.append(x)
    
    def pop(self):
        """
        :rtype: int
        """
        self.move()
        return self.out_stack.pop()
    
    def peek(self):
        """
        :rtype: int
        """
        self.move()
        return self.out_stack[-1]
    
    def empty(self):
        """
        :rtype: bool
        """
        return not self.in_stack and not self.out_stack

    def move(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())