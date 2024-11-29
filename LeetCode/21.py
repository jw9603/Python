# 21. Merge Two Sorted Lists
# https://leetcode.com/problems/merge-two-sorted-lists/description/?envType=problem-list-v2&envId=linked-list&difficulty=EASY

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    @staticmethod
    def from_list(values): # values : List
        head = ListNode()
        current = head
        for value in values:
            current.next = ListNode(value)
            current = current.next
        return head.next
    
    def to_list(self):
        result = []
        current = self
        while current:
            result.append(current.val)
            current = current.next
        return result
    
        
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        # https://leetcode.com/problems/merge-two-sorted-lists/submissions/1465462983
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Base Case
        if list1 is None or list2 is None:
            return list1 or list2
        
        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2

    # def mergeTwoLists(self, list1, list2):
        # https://leetcode.com/problems/merge-two-sorted-lists/submissions/1465462206
    #     """
    #     :type list1: Optional[ListNode]
    #     :type list2: Optional[ListNode]
    #     :rtype: Optional[ListNode]
    #     """
    #     head = ListNode()
    #     start = head
        
    #     while list1 and list2:
            
    #         if list1.val < list2.val:
    #             start.next = list1
    #             list1 = list1.next
    #         else:
    #             start.next = list2
    #             list2 = list2.next
            
    #         start = start.next
        
    #     if list1:
    #         start.next = list1
    #     if list2:
    #         start.next = list2
        
    #     return head.next
if __name__ == '__main__':
    
    
    # Example inputs
    example1_list1 = ListNode.from_list([1, 2, 4])
    example1_list2 = ListNode.from_list([1, 3, 4])

    example2_list1 = ListNode.from_list([])
    example2_list2 = ListNode.from_list([])

    example3_list1 = ListNode.from_list([])
    example3_list2 = ListNode.from_list([0])

    # Create a Solution instance and test the method
    solution = Solution()
    result1 = solution.mergeTwoLists(example1_list1, example1_list2)
    result2 = solution.mergeTwoLists(example2_list1, example2_list2)
    result3 = solution.mergeTwoLists(example3_list1, example3_list2)
    
    
    result1 = result1.to_list() if result1 else []
    result2 = result2.to_list() if result2 else []
    result3 = result3.to_list() if result3 else []
    
    print(f"Example1 : {result1}")
    print(f"Example2 : {result2}")
    print(f"Example3 : {result3}")
