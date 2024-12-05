# 24. Swap Nodes in Pairs
# https://leetcode.com/problems/swap-nodes-in-pairs/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    # 1. Iterative
    def swapPairs_iterative(self, head):
        # https://leetcode.com/problems/swap-nodes-in-pairs/submissions/1470789178
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(next=head)
        prev = dummy
        
        while prev.next and prev.next.next:
            
            first = prev.next
            second = prev.next.next
            
            prev.next = second
            first.next = second.next
            second.next = first
            
            prev = first
        return dummy.next
    
    # 2. Recursion
    def swapPairs_recursion(self, head):
        # https://leetcode.com/problems/swap-nodes-in-pairs/submissions/1470802663
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head
        
        first = head
        second = head.next
        
        first.next = self.swapPairs_recursion(second.next)
        second.next = first
        
        return second

def print_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

def create_list(values):
    dummy = ListNode()
    current =dummy
    for value in values:
        current.next = ListNode(value)
        current = current.next
    return dummy.next

if __name__ == '__main__':
    # 테스트 케이스
    test_cases = [
        [1, 2, 3, 4],  # 출력: [2, 1, 4, 3]
        [],            # 출력: []
        [1],           # 출력: [1]
        [1, 2, 3],     # 출력: [2, 1, 3]
    ]

    for i, values in enumerate(test_cases):
        head = create_list(values)
        solution = Solution()
        print(f"Test Case {i + 1}: {values}")
        print("  Iterative:", print_list(solution.swapPairs_iterative(head)))

        head = create_list(values)
        print("  Recursive:", print_list(solution.swapPairs_recursion(head)))
    