# 114. Flatten Binary Tree to Linked List
# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
    def to_list(self):
        result = []
        current = self
        while current:
            result.append(current.val)
            current = current.right
        return result
class Solution(object):
    # 1. Recursion
    def flatten_recursive(self, root):
        # https://leetcode.com/problems/flatten-binary-tree-to-linked-list/submissions/1470756133
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        
        nodes = []
        def preorder(node):
            if node:
                nodes.append(node)
                preorder(node.left)
                preorder(node.right)
        
        preorder(root)
        for i in range(len(nodes)-1):
            nodes[i].right = nodes[i + 1]
            nodes[i].left = None
    # 2. Stack
    def flatten_stack(self, root):
        # https://leetcode.com/problems/flatten-binary-tree-to-linked-list/submissions/1470755853
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        
        stack = [root]
        
        while stack:
            current = stack.pop()
            
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
            
            if stack:
                current.right = stack[-1]
            current.left = None

def build_tree(values):
    if not values:
        return None
    nodes = [TreeNode(val) if val is not None else None for val in values]
    for i, node in enumerate(nodes):
        if node:
            left_idx = 2 * i + 1
            right_idx = 2 * i + 2
            if left_idx < len(nodes):
                node.left = nodes[left_idx]
            if right_idx < len(nodes):
                node.right = nodes[right_idx]
    return nodes[0]


if __name__ == '__main__':
    # Test cases
    test_cases = [
        ([1, 2, 5, 3, 4, None, 6], [1, None, 2, None, 3, None, 4, None, 5, None, 6]),
        ([], []),
        ([0], [0])
    ]
    
    # Run tests
    for i, (input_tree, expected_output) in enumerate(test_cases):
        print(f"Test Case {i + 1}:")
        root = build_tree(input_tree)

        # Test recursive method
        solution = Solution()
        root_recursive = build_tree(input_tree)  # Rebuild tree for a fresh start
        solution.flatten_recursive(root_recursive)
        result_recursive = root_recursive.to_list() if root_recursive else []
        print(f"  Recursive Output: {result_recursive} (Expected: {expected_output})")

        # Test stack method
        root_stack = build_tree(input_tree)  # Rebuild tree for a fresh start
        solution.flatten_stack(root_stack)
        result_stack = root_stack.to_list() if root_stack else []
        print(f"  Stack Output: {result_stack} (Expected: {expected_output})")