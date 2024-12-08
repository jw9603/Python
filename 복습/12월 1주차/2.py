# 2. Add Two Numbers
# https://leetcode.com/problems/add-two-numbers/description/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):

    # 1. iterable
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()
        curr = dummy
        carry = 0
        
        while carry or l1 or l2:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            
            curr.next = ListNode(carry % 10)
            carry //= 10
            curr = curr.next
        
        return dummy.next
    # 2. Recursion
    def addTwoNumbers(self, l1, l2, carry):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # base case
        if not l1 and not l2 and carry == 0:
            return None
        
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        
        total = val1 + val2 + carry
        
        node = ListNode(total % 10)
        
        node.next = self.addTwoNumbers(
            l1.next if l1 else None,
            l2.next if l2 else None,
            total // 10
        )
        return node
    
    