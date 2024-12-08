# 160. Intersection of Two Linked Lists
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    # 1. Hash Table
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        
        node_set = set()
        
        while headA:
            node_set.add(headA)
            headA = headA.next
        while headB:
            if headB in node_set:
                return headB
            
            headB = headB.next
        return None
    # 2. Two Pinter
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        a, b = headA, headB
        while a != b:
            if a:
                a = a.next
            else:
                a = headB
            if b:
                b = b.next
            else:
                b = headA
        return a
    
    