# 234. Palindrome Linked List
# https://leetcode.com/problems/palindrome-linked-list/description/?envType=problem-list-v2&envId=linked-list&difficulty=EASY

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    # 1. Linked List
    def isPalindrome1(self, head):
        # https://leetcode.com/problems/palindrome-linked-list/submissions/1467936746
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        a = []
        curr = head
        while curr:
            a.append(curr.val)
            curr = curr.next
        
        if a != list(reversed(a)):
            return False
        return True
    
    # 2. Two Pointer
    def isPalindrome2(self, head):
        # https://leetcode.com/problems/palindrome-linked-list/submissions/1467944691
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node
        
        l, r = head, prev
        while r:
            if l.val != r.val:
                return False
            l = l.next
            r = r.next
        
        return True
    # 3. Stack
    def isPalindrome3(self, head):
        # https://leetcode.com/problems/palindrome-linked-list/submissions/1467948467
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        stack = []
        curr = head
        
        while curr:
            stack.append(curr.val)
            curr = curr.next
            
        curr = head
        while curr:
            if curr.val != stack.pop():
                return False
            curr = curr.next
        return True
    
    # 4. Recursive
    def isPalindrome4(self, head):
        # https://leetcode.com/problems/palindrome-linked-list/submissions/1467954119
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        self.pointer = head
        
        def recursive_check(curr):
            
            # Base Case
            if not curr:
                return True
            
            if not recursive_check(curr.next):
                return False
            
            if curr.val != self.pointer.val:
                return False
            
            self.pointer = self.pointer.next
            
            return True
        
        return recursive_check(head)

# 연결 리스트 유틸리티 함수
def list_to_linked_list(arr):
    if not arr:
        return None
    
    head = ListNode(arr[0])
    curr = head
    
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    
    return head

if __name__ == '__main__':
    a = Solution()
    
    # Example1 리스트
    example1_values = [1, 2, 2, 1]
    example2_values = [1, 2]
    
    print(f"<Example1 Result>")
    example1 = list_to_linked_list(example1_values)  # 초기화
    print(f"Example1 result using Linked List method: {a.isPalindrome1(example1)}")
    
    example1 = list_to_linked_list(example1_values)  # 초기화
    print(f"Example1 result using Two Pointer method: {a.isPalindrome2(example1)}")
    
    example1 = list_to_linked_list(example1_values)  # 초기화
    print(f"Example1 result using Stack method: {a.isPalindrome3(example1)}")
    
    example1 = list_to_linked_list(example1_values)  # 초기화
    print(f"Example1 result using Recursive method: {a.isPalindrome4(example1)}")
    
    print()
    
    print(f"<Example2 Result>")
    example2 = list_to_linked_list(example2_values)  # 초기화
    print(f"Example2 result using Linked List method: {a.isPalindrome1(example2)}")
    
    example2 = list_to_linked_list(example2_values)  # 초기화
    print(f"Example2 result using Two Pointer method: {a.isPalindrome2(example2)}")
    
    example2 = list_to_linked_list(example2_values)  # 초기화
    print(f"Example2 result using Stack method: {a.isPalindrome3(example2)}")
    
    example2 = list_to_linked_list(example2_values)  # 초기화
    print(f"Example2 result using Recursive method: {a.isPalindrome4(example2)}")

    