# 24. Swap Nodes in Pairs
# https://leetcode.com/problems/swap-nodes-in-pairs/description/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    # 1. Recursive
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head
        
        first = head
        second = head.next
        
        first.next = self.swapPairs(second.next)
        second.next = first
        
        return second
    # 2. Iterative
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(next=head)
        prev = dummy
        
        while prev.next and prev.next.next:
            first = prev.next
            second = prev.next.next
            
            prev.next = second
            first.next = second.next
            second.next = first
            
            prev = first
        return dummy.next
    