# 141. Linked List Cycle
# https://leetcode.com/problems/linked-list-cycle/description/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    

    @staticmethod
    def from_list_with_cycle(values, pos):
        """
        Creates a linked list with a cycle based on the given pos.
        :param values: List[int] - Values for the linked list nodes.
        :param pos: int - Index where the tail connects to form a cycle (-1 for no cycle).
        :return: ListNode - Head of the linked list with the specified cycle.
        """
        if not values:
            return None

        head = ListNode(values[0])
        current = head
        cycle_node = None

        for i, value in enumerate(values[1:], start=1):
            current.next = ListNode(value)
            current = current.next
            if i == pos:
                cycle_node = current

        # Connect tail to the cycle node if pos is valid
        if pos != -1:
            current.next = cycle_node

        return head


    
        
class Solution(object):
    # # 1. Hash Table
    def hasCycle(self, head):
        # https://leetcode.com/problems/linked-list-cycle/submissions/1465481746
        """
        :type head: ListNode
        :rtype: bool
        """
        node_set = set()
        
        while head:
            
            if head in node_set:
                return True
            
            node_set.add(head)
            head = head.next
        return False

    # # 2. Two Pointer
    def hasCycle(self, head):
        # https://leetcode.com/problems/linked-list-cycle/submissions/1465481577
        """
        :type head: ListNode
        :rtype: bool
        """
        # first는 1칸
        # second는 2칸
        first = head
        second = head
        
        while second and second.next:
            first = first.next
            second = second.next.next
            
            if first == second:
                return True
        return False

if __name__ == '__main__':
    
    example1 = ListNode.from_list_with_cycle([3, 2, 0, -4], 1)
    example2 = ListNode.from_list_with_cycle([1, 2], 0)
    example3 = ListNode.from_list_with_cycle([1], -1)
    
    solution = Solution()
    
    result1 = solution.hasCycle(example1)
    result2 = solution.hasCycle(example2)
    result3 = solution.hasCycle(example3)
    
    print(f"Example1 : {result1}")
    print(f"Example2 : {result2}")
    print(f"Example3 : {result3}")

        