# 142. Linked List Cycle II
# https://leetcode.com/problems/linked-list-cycle-ii/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution(object):
    # 1. Hash Table
    def detectCycle1(self, head):
        # https://leetcode.com/problems/linked-list-cycle-ii/submissions/1471492958
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node_set = set()
        
        while head:
            if head in node_set:
                return head
            node_set.add(head)
            head = head.next
        return None
    
    # 2. Two Pointer
    def detectCycle2(self, head):
        # https://leetcode.com/problems/linked-list-cycle-ii/submissions/1471492811
        """
        :type head: ListNode
        :rtype: ListNode
        """
        s, f = head, head
        
        while f and f.next:
            s = s.next
            f = f.next.next
            
            if s == f:
                s = head
                break
        else:
            return None
        
        while s!= f:
            s = s.next
            f = f.next
        return s
    
if __name__ == '__main__':
    # 노드 생성
    head = ListNode(3)
    node2 = ListNode(2)
    node3 = ListNode(0)
    node4 = ListNode(-4)
    head.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2  # 사이클 연결
    
    solution = Solution()

print(f"hash 방법: {solution.detectCycle1(head).val}")  # 출력: 2
print(f"Two Pointer 방법: {solution.detectCycle2(head).val}")  # 출력: 2