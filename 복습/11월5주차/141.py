# 141. Linked List Cycle
# https://leetcode.com/problems/linked-list-cycle/description/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution(object):
    # # 1. Hash Table
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        node_set = set()
        while head:
            if head in node_set:
                return True
            node_set.add(head)
            head = head.next

    # 2. Two Pointer
    def hashCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        f, s = head, head
        while s and s.next:
            f = f.next
            s = s.next.next
            
            if f == s:
                return True
        return False