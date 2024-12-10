# 142. Linked List Cycle 2
# https://leetcode.com/problems/linked-list-cycle-ii/description/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    
    # 1. Hash Table
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node_set = set()
        
        while head:
            if head in node_set:
                return head
            node_set.add(head)
            head = head.next
        return None

    # 2. Two Pointer
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        s, f = head, head
        
        while f and f.next:
            s = s.next
            f = f.next.next
            
            if s == f:
                s = head
                break
        else:
            return None
        
        while s != f:
            s = s.next
            f = f.next
        return s
    