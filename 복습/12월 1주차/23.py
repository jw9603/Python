# 23. Merge k Sorted Lists
# https://leetcode.com/problems/merge-k-sorted-lists/description/
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from heapq import heappop, heappush
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """

        if not lists or len(lists) == 0:
            return None
        heap = []

        for i, l in enumerate(lists):
            if l:
                heappush(heap,(l.val, i, l))
        dummy = ListNode()
        current = dummy

        while heap:
            val, i, node = heappop(heap)
            current.next = node
            current = current.next
            if node.next:
                heappush(heap,(node.next.val, i, node.next))
        return dummy.next