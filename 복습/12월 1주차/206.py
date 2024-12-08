# 206. Reverse Linked List
# https://leetcode.com/problems/reverse-linked-list/description/?envType=problem-list-v2&envId=linked-list&difficulty=EASY

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    # 1. Iterative
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prev = None
        curr = head
        
        while curr:
            next_node = curr.next 
            curr.next = prev
            prev = curr
            curr = next_node
        return prev
    # 2. Recursive
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        def recursive_reversed(prev, node):
            if node:
                next_node, node.next = node.next, prev
                return recursive_reversed(node, next_node)
            else:
                return prev
        
        return recursive_reversed(None, head)
    