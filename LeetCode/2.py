# 2. Add Two Numbers
# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    # 1. Linked List
    def addTwoNumbers(self, l1, l2):
        # https://leetcode.com/problems/add-two-numbers/submissions/1469870730/
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()  # 더미 노드 생성
        curr = dummy  # 현재 노드 포인터
        carry = 0  # 올림 값 초기화

        # l1, l2 또는 carry가 존재하는 동안 반복
        while carry or l1 or l2:
            if l1:
                carry += l1.val
                l1 = l1.next  # l1의 다음 노드로 이동
            if l2:
                carry += l2.val
                l2 = l2.next  # l2의 다음 노드로 이동
            
            # 현재 자리수 계산 및 연결
            curr.next = ListNode(carry % 10)  # 자릿수 값 생성
            carry //= 10  # 올림값 업데이트
            
            # 다음 노드로 이동
            curr = curr.next
        
        # 결과로 더미 노드의 다음 노드 반환
        return dummy.next
    
    # 2. Linked List
    def addTwoNumbers(self, l1, l2, carry=0):
        # https://leetcode.com/problems/add-two-numbers/submissions/1469872346
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not l1 and not l2 and carry == 0:
            return None
        
        val1 = l1.val if val1 else 0
        val2  = l2.val if val2 else 0
        total = val1 + val2 + carry
        
        node = ListNode(total % 10)
        node.next = self.addTwoNumbers(
            l1.next if l1 else None,
            l2.next if l2 else None,
            total // 10
        )
        
        return node
    
    
def list_to_linked_list(lst):
    dummy = ListNode()
    curr = dummy
    for num in lst:
        curr.next = ListNode(num)
        curr = curr.next
    return dummy.next

def linked_list_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


if __name__ == "__main__":
    # 테스트 입력
    l1 = list_to_linked_list([2, 4, 3])
    l2 = list_to_linked_list([5, 6, 4])

    # 솔루션 호출
    solution = Solution()
    result = solution.addTwoNumbers(l1, l2)
    
    print(result)

    # 결과 출력
    print(linked_list_to_list(result))  # Output: [7, 0, 8]

    
