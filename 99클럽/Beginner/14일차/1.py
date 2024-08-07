# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def isSubtreeSymmetric(left,right):
            if not left and not right: # 왼쪽, 오른쪽 둘 다 없으면
                return True
            elif not left or not right: # 둘 중 하나만 있으면
                return False
            else: # 둘 다 있으면
                return left.val == right.val and isSubtreeSymmetric(left.left, right.right) and isSubtreeSymmetric(left.right, right.left)
