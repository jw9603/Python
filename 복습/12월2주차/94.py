# LeetCode 94. Binary Tree Inorder Traversal
# https://leetcode.com/problems/binary-tree-inorder-traversal/description/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    # 1. Recursion
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:
            return []
        visited = []
        def inorder(root):
            if root:
                inorder(root.left)
                visited.append(root.val)
                inorder(root.right)
            return visited
        return inorder(root)
    # 2. Stack
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:
            return []
        stack = []
        visited = []
        cur_node = root
        
        while stack or cur_node:
            while cur_node:
                stack.append(cur_node)
                cur_node = cur_node.left
            cur_node = stack.pop()
            visited.append(cur_node.val)
            
            cur_node = cur_node.right
        return visited
    