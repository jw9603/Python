# 160. Intersection of Two Linked Lists
# https://leetcode.com/problems/intersection-of-two-linked-lists/description/?envType=problem-list-v2&envId=linked-list&difficulty=EASY

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    # # 1. Hash Table
    def getIntersectionNode(self, headA, headB):
        # https://leetcode.com/problems/intersection-of-two-linked-lists/submissions/1468999186
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

    # # 2. Two Pointer
    def getIntersectionNode(self, headA, headB):
        # https://leetcode.com/problems/intersection-of-two-linked-lists/submissions/1468996370
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        
        a, b = headA, headB
        while a != b:
            
            if not a:
                a = headB
            else:
                a = a.next
            
            if not b:
                b = headA
            else:
                b = b.next
        return a


  