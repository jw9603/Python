# 234. Palindrome Linked List
# https://leetcode.com/problems/palindrome-linked-list/description/?envType=problem-list-v2&envId=linked-list&difficulty=EASY

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    
    # 1. Linked List
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        result = []
        curr = head
        while curr:
            result.append(curr.val)
            curr = curr.next
        
        if result == list(reversed(result)):
            return True
        return False
    # 2. Two pointer
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        s, f = head, head
        
        while f and f.next:
            s = s.next
            f = f.next.next
        
        prev = None
        while s:
            next_node = s.next
            s.next = prev
            prev = s
            s = next_node
        
        l, r = head, prev
        while r:
            if l.val != r.val:
                return False
            l = l.next
            r = r.next
    # 3. Stack
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        stack = []
        curr = head
        while curr:
            stack.append(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            if curr.val != stack.pop():
                return False
            curr = curr.next
        return True
    # 4. Recursion
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        self.pointer = head
        
        def recursive_check(node):
            # base case
            if not node:
                return True
            
            if not recursive_check(node.next):
                return False
            if node.val != self.pointer.val:
                return False
            
            self.pointer = self.pointer.next
            return True
        
        return recursive_check(head)
        