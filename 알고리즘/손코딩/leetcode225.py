# LeetCode 225. Implement Stack using Queues
# https://leetcode.com/problems/implement-stack-using-queues/description/
from collections import deque
class MyStack(object):

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
    
    def push(self, x):
        '''
        :type x: int
        :rtype: None
        '''
        self.q2.append(x)

        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1
    
    def pop(self):
        '''
        :rtype: int
        '''
        return self.q1.popleft()

    def top(self):
        '''
        :rtype: int
        '''
        return self.q1[0]
    
    def empty(self):
        '''
        :rtype: bool
        '''
        return not self.q1 and not self.q2