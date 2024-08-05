# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        while root:
            if root.val < val:
                if root.right:
                    root = root.right
                else:
                    return
            elif root.val > val:
                if root.left:
                    root = root.left
                else:
                    return
            else:
                return root