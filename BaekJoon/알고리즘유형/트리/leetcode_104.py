# LeetCode 104. Maximum Depth of Binary Tree
# https://leetcode.com/problems/maximum-depth-of-binary-tree/
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
#################### Level Order Traversal ####################
from collections import deque
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        max_depth = 0
        if root is None:
            return 0
        q = deque()
        q.append((root, 1))
        while q:
            cur_node, cur_depth = q.popleft()
            max_depth = max(max_depth, cur_depth)
            if cur_node.left:
                q.append((cur_node.left, cur_depth + 1))
            if cur_node.right:
                q.append((cur_node.right, cur_depth + 1))
        return max_depth
#################### Level Order Traversal ####################

#################### Post Order Traversal ####################
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if root is None:
            return 0
        
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        
        return max(left_depth, right_depth) + 1
#################### Post Order Traversal ####################

#################### Pre Order Traversal ####################
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.max_depth = 0
        
        def preorder(node, depth):
            if not node:
                return 0
            self.max_depth = max(depth, self.max_depth)
            preorder(node.left, depth + 1)
            preorder(node.right, depth + 1)
        
        preorder(root, 1)
        return self.max_depth
#################### Pre Order Traversal ####################

#################### In Order Traversal ####################
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.max_depth = 0
        
        def inorder(node, depth):
            if not node:
                return 0
            inorder(node.left, depth + 1)
            self.max_depth = max(depth, self.max_depth)
            inorder(node.right, depth + 1)
        
        inorder(root, 1)
        return self.max_depth
#################### In Order Traversal ####################