# 23. Merge k Sorted Lists
# https://leetcode.com/problems/merge-k-sorted-lists/ 

from heapq import heappop, heappush
import sys
sys.setrecursionlimit(10**6)  # 재귀 깊이를 1,000,000으로 늘림

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    
    # 1. Priority Queue
    def mergeKLists1(self, lists):
        # https://leetcode.com/problems/merge-k-sorted-lists/submissions/1471587504
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
                
    # 2. Divide and Conquer
    def mergeKLists2(self, lists):
        # https://leetcode.com/problems/merge-k-sorted-lists/submissions/1471581479
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        
        mid = len(lists) // 2
        
        left = self.mergeKLists2(lists[:mid])
        right = self.mergeKLists2(lists[mid:])
        return self.mergeTwoLists(left, right)
        
    # def mergeTwoLists(self, l1, l2):
        
    #     if not l1 or not l2:
    #         return l1 or l2
        
    #     if l1.val < l2.val:
    #         l1.next = self.mergeTwoLists(l1.next, l2)
    #         return l1
    #     else:
    #         l2.next = self.mergeTwoLists(l1, l2.next)
    #         return l2
    def mergeTwoLists(self,l1, l2):
        dummy = ListNode()
        curr = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        
        curr.next = l1 or l2
        return dummy.next

def print_linked_list(head):
    """Helper function to print the linked list."""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

def create_linked_list(arr):
    """Helper function to create a linked list from a list."""
    if not arr:
        return None
    dummy = ListNode()
    current = dummy
    for val in arr:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

if __name__ == '__main__':
    # Test cases
    test_cases = [
        # Input: k sorted linked lists
        [[1, 4, 5], [1, 3, 4], [2, 6]],  # Expected: [1, 1, 2, 3, 4, 4, 5, 6]
        [],                              # Expected: []
        [[]],                            # Expected: []
        [[1], [0]],                      # Expected: [0, 1]
    ]

    # Instantiate the solution object
    solution = Solution()

    # Test the two implementations
    for i, test in enumerate(test_cases):
        print(f"Test Case {i + 1}:")

        # Create linked lists for the test case
        linked_lists = [create_linked_list(l) for l in test]

        # Test Priority Queue implementation
        print("  Priority Queue Approach:")
        result = solution.mergeKLists1(linked_lists)
        print("  Output:", print_linked_list(result))

        # Test Divide and Conquer implementation
        print("  Divide and Conquer Approach:")
        result = solution.mergeKLists2(linked_lists)
        print("  Output:", print_linked_list(result))
        print("-" * 30)
