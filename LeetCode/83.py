# 83. Remmove Duplicates from Sorted List
# https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/?envType=problem-list-v2&envId=linked-list&difficulty=EASY

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        # https://leetcode.com/problems/remove-duplicates-from-sorted-list/submissions/1468959575
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        if not head:
            return None

        curr = head
        while curr:
            while curr.next and curr.next.val == curr.val:
                curr.next = curr.next.next
            curr = curr.next
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
    
    example1 = [1, 1, 2]
    example2 = [1, 1, 2, 3, 3]
    
    # Example1
    head1 = list_to_linked_list(example1)
    result1 = a.deleteDuplicates(head1)
    
    # Example2
    head2 = list_to_linked_list(example2)
    result2 = a.deleteDuplicates(head2)
    
    result1 = linked_list_to_list(result1)
    result2 = linked_list_to_list(result2)
    
    print(f"<Example1 Result>")
    print(f"Example1 Result: {result1}")
    print()
    print(f"<Example2 Result>")
    print(f"Example2 Result: {result2}")