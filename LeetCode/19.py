# 19. Remove Nth Node From End of List
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        # https://leetcode.com/problems/remove-nth-node-from-end-of-list/submissions/1469890775
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(next=head)
        
        s, f = dummy, dummy
        
        for _ in range(n + 1):
            f = f.next
        
        while f:
            s = s.next
            f = f.next
        s.next = s.next.next
        
        return dummy.next
    
def list_to_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result
    
if __name__ == '__main__':
    # Test cases
    solution = Solution()

    # Example 1
    head1 = list_to_linked_list([1, 2, 3, 4, 5])
    n1 = 2
    result1 = solution.removeNthFromEnd(head1, n1)
    print("Example 1:", linked_list_to_list(result1))  # Output: [1, 2, 3, 5]

    # Example 2
    head2 = list_to_linked_list([1])
    n2 = 1
    result2 = solution.removeNthFromEnd(head2, n2)
    print("Example 2:", linked_list_to_list(result2))  # Output: []

    # Example 3
    head3 = list_to_linked_list([1, 2])
    n3 = 1
    result3 = solution.removeNthFromEnd(head3, n3)
    print("Example 3:", linked_list_to_list(result3))  # Output: [1]

    
    