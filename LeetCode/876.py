# 876. Middle of the Linked List
# https://leetcode.com/problems/middle-of-the-linked-list/description/?envType=problem-list-v2&envId=linked-list&difficulty=EASY

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def middleNode(self, head):
        # https://leetcode.com/problems/middle-of-the-linked-list/submissions/1469832333
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        s, f = head, head
        while f and f.next:
            s = s.next
            f = f.next.next
        return s
    
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
    a = Solution()
    
    example1 = [1, 2, 3, 4, 5]
    example2 = [1, 2, 3, 4, 5, 6]
    
    # Example1
    head1 = list_to_linked_list(example1)
    result1 = a.middleNode(head1)
    result1 = linked_list_to_list(result1)
    
    # Example2
    head2 = list_to_linked_list(example2)
    result2 = a.middleNode(head2)
    result2 = linked_list_to_list(result2)
    
    print(f"<Example1 Result>")
    print(f"Example1 Result: {result1}")
    print()
    print(f"<Example2 Result>")
    print(f"Example2 Result: {result2}")
