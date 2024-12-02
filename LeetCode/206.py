# 206. Reverse Linked List
# https://leetcode.com/problems/reverse-linked-list/description/?envType=problem-list-v2&envId=linked-list&difficulty=EASY

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):

    # 1. iterative
    def reverseList1(self, head):
        # https://leetcode.com/problems/reverse-linked-list/submissions/1467929284
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prev = None
        curr = head
        while curr:
            next_node = curr.next  # 현재 노드의 다음 노드를 저장
            curr.next = prev  # 현재 노드의 다음 포인터를 뒤집어서 이전 노드를 가리키게 함
            prev = curr  # 결과 리스트의 헤드를 현재 노드로 업데이트
            curr = next_node  # 다음 노드로 이동
        return prev

    
    # # 2. recursion
    def reverseList2(self, head):
        # https://leetcode.com/problems/reverse-linked-list/submissions/1467928535
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        def recursive_reversed(prev, node):
            if node:
                next_node, node.next = node.next, prev  # 다음 노드를 저장하고 포인터 뒤집기
                return recursive_reversed(node, next_node)  # 현재 노드를 prev로, 다음 노드를 node로 진행
            else:
                return prev  # node가 None일 때, 이전 노드(prev)가 새 헤드가 됨
        return recursive_reversed(None, head)
    
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
    
    example1 = [1, 2, 3, 4, 5]
    example2 = [1, 2]
    example3 = []
    
    # Example1
    head1 = list_to_linked_list(example1)
    result1_1 = a.reverseList1(head1)
    head1 = list_to_linked_list(example1)  # 원래 상태로 복원
    result1_2 = a.reverseList2(head1)
    
    # Example2
    head2 = list_to_linked_list(example2)
    result2_1 = a.reverseList1(head2)
    head2 = list_to_linked_list(example2)  # 원래 상태로 복원
    result2_2 = a.reverseList2(head2)
    
    # Example3
    head3 = list_to_linked_list(example3)
    result3_1 = a.reverseList1(head3)
    head3 = list_to_linked_list(example3)  # 원래 상태로 복원
    result3_2 = a.reverseList2(head3)
    
    # Convert linked list back to Python list for output
    result1_1 = linked_list_to_list(result1_1)
    result1_2 = linked_list_to_list(result1_2)
    result2_1 = linked_list_to_list(result2_1)
    result2_2 = linked_list_to_list(result2_2)
    result3_1 = linked_list_to_list(result3_1)
    result3_2 = linked_list_to_list(result3_2)
    
    print(f"<Example1 Result>")
    print(f"Example1 Result using iterative method: {result1_1}")
    print(f"Example1 Result using recursive method: {result1_2}")
    print()
    print(f"<Example2 Result>")
    print(f"Example2 Result using iterative method: {result2_1}")
    print(f"Example2 Result using recursive method: {result2_2}")
    print()
    print(f"<Example3 Result>")
    print(f"Example3 Result using iterative method: {result3_1}")
    print(f"Example3 Result using recursive method: {result3_2}")
