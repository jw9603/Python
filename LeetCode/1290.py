# 1290. Convert Binary Number in a Linked List to Integer
# https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/description/?envType=problem-list-v2&envId=linked-list&difficulty=EASY

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def getDecimalValue(self, head):
        # https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/submissions/1469842705
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        ans = ""
        while head:
            ans += str(head.val)
            head = head.next
        return int(ans, 2)

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


if __name__ == '__main__':
    a = Solution()
    
    example1 = [1, 0, 1]
    example2 = [0]
    
    # Example1
    head1 = list_to_linked_list(example1)
    result1 = a.getDecimalValue(head1)
    
    # Example2
    head2 = list_to_linked_list(example2)
    result2 = a.getDecimalValue(head2)

    
    print(f"<Example1 Result>")
    print(f"Example1 Result: {result1}")
    print()
    print(f"<Example2 Result>")
    print(f"Example2 Result: {result2}")