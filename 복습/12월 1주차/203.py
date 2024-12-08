# 203. Remove Linked List Elements
# https://leetcode.com/problems/remove-linked-list-elements/description/?envType=problem-list-v2&envId=linked-list&difficulty=EASY

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    # 1. Linked List
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        
        dummy = ListNode(next=head)
        curr = dummy
        
        while curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        
        return dummy.next
    
    # 2. Recursion
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        # base case
        if not head:
            return None
        
        head.next = self.removeElements(head.next,val)
        
        if head.val == val:
            return head.next
        
        
        return head
        
        
    
        