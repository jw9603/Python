# 114. Flatten Binary Tree to Linked List
# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return 
        nodes = []
        def preorder(root):
            if root:
                nodes.append(root)
                preorder(root.left)
                preorder(root.right)
        
        preorder(root=root)
        for i in range(len(nodes) - 1):
            nodes[i].right = nodes[i + 1]
            nodes[i].left = None
    def flatten(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        stack = [root]
        while stack:
            curr = stack.pop()
            
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)
            if stack:
                curr.right = stack[-1]
            curr.left = None