# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        # Inorder traversal : 중위 순회로, 왼 -> root -> 오
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        def inorder(root):
            if root:
                inorder(root.left)
                result.append(root.val)
                inorder(root.right)
        
        inorder(root)
        return result

################# 다른 풀이 ########################
class Solution:
    def inorderTraversal(self, root):
        res = []
        stack = []
        curr = root
        while curr or stack: 
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right
        return res
################# 다른 풀이 ########################