# 203. Remove Linked List Elements
# https://leetcode.com/problems/remove-linked-list-elements/?envType=problem-list-v2&envId=linked-list&difficulty=EASY
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    # 1. Linked List using dummy
    def removeElements1(self, head, val):
        # https://leetcode.com/problems/remove-linked-list-elements/submissions/1469021357
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        
        dummy = ListNode()
        dummy.next = head
        curr = dummy
        
        while curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return dummy.next
                
    # 2. Linked List not using dummy
    def removeElements2(self, head, val):
        # https://leetcode.com/problems/remove-linked-list-elements/submissions/1469019847
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        while head and head.val == val:
            head = head.next
        
        curr = head
        while curr and curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head
            
    # # 3. Recursion
    def removeElements3(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        # base case
        if not head:
            return None
        
        head.next = self.removeElements3(head.next, val)
        
        if head.val == val:
            return head.next
        
        return head
    
def list_to_linked_list(arr):
    """Python 리스트를 연결 리스트로 변환"""
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    
    return head

def linked_list_to_list(head):
    """연결 리스트를 Python 리스트로 변환"""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

if __name__ == '__main__':
    a = Solution()
    
    example1 = [1,2,6,3,4,5,6]
    example2 = []
    example3 = [7, 7, 7, 7]
    val1 = 6
    val2 = 1
    val3 = 7
    
    # Example1
    head1 = list_to_linked_list(example1)
    result1_1 = a.removeElements1(head1,val1)
    head1 = list_to_linked_list(example1)  # 원래 상태로 복원
    result1_2 = a.removeElements2(head1,val1)
    head1 = list_to_linked_list(example1)  # 원래 상태로 복원
    result1_3 = a.removeElements2(head1,val1)
    
    # Example2
    head2 = list_to_linked_list(example2)
    result2_1 = a.removeElements1(head2,val2)
    head1 = list_to_linked_list(example2)  # 원래 상태로 복원
    result2_2 = a.removeElements2(head2,val2)
    head1 = list_to_linked_list(example2)  # 원래 상태로 복원
    result2_3 = a.removeElements2(head2,val2)
    
    # Example3
    head3 = list_to_linked_list(example2)
    result3_1 = a.removeElements3(head2,val3)
    head3 = list_to_linked_list(example2)  # 원래 상태로 복원
    result3_2 = a.removeElements3(head2,val3)
    head3 = list_to_linked_list(example2)  # 원래 상태로 복원
    result3_3 = a.removeElements3(head2,val3)
    
    # Convert linked list back to Python list for output
    result1_1 = linked_list_to_list(result1_1)
    result1_2 = linked_list_to_list(result1_2)
    result1_3 = linked_list_to_list(result1_3)
    result2_1 = linked_list_to_list(result2_1)
    result2_2 = linked_list_to_list(result2_2)
    result2_3 = linked_list_to_list(result2_3)
    result3_1 = linked_list_to_list(result3_1)
    result3_2 = linked_list_to_list(result3_2)
    result3_3 = linked_list_to_list(result3_3)
    
    print(f"<Example1 Result>")
    print(f"Example1 Result using Linked List dummy method: {result1_1}")
    print(f"Example1 Result using Linked List method: {result1_2}")
    print(f"Example1 Result using Recursive method: {result1_3}")
    print()
    print(f"<Example2 Result>")
    print(f"Example2 Result using Linked List dummy method: {result2_1}")
    print(f"Example2 Result using Linked List method: {result2_2}")
    print(f"Example1 Result using Recursive method: {result2_3}")
    print()
    print(f"<Example3 Result>")
    print(f"Example3 Result using Linked List dummy method: {result3_1}")
    print(f"Example3 Result using Linked List method: {result3_2}")
    print(f"Example1 Result using Recursive method: {result3_3}")