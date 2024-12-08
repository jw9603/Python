# 876. Middle of the Linked List
# https://leetcode.com/problems/middle-of-the-linked-list/description/?envType=problem-list-v2&envId=linked-list&difficulty=EASY

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def middleNode(self, head):
        
        s, f = head, head
        while f and f.next:
            s = s.next
            f = f.next.next
        return s