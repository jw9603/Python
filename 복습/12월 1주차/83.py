# 83. Remove Duplicates from Sorted List
# https://leetcode.com/problems/remove-duplicates-from-sorted-list/?envType=problem-list-v2&envId=linked-list&difficulty=EASY

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return None
        
        curr = head
        
        while curr:
            if curr.next and curr.next.val == curr.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head