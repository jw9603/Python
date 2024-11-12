# 236. Lowest Common Ancestor of a Binary Tree
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if root is None:
            return None
        
        if root.val == p.val or root.val == q.val:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        if left and right:
            return root
        return left or right

from collections import deque

def build_tree(nodes):
    if not nodes or nodes[0] is None:
        return None
    
    root = TreeNode(nodes[0])
    queue = deque([root])
    idx = 1
    
    while queue and idx < len(nodes):
        node = queue.popleft()
        
        # Left child
        if idx < len(nodes) and nodes[idx] is not None:
            node.left = TreeNode(nodes[idx])
            queue.append(node.left)
        idx += 1
        
        # Right child
        if idx < len(nodes) and nodes[idx] is not None:
            node.right = TreeNode(nodes[idx])
            queue.append(node.right)
        idx += 1

    return root

def run_example(root_vals, p_val, q_val):
    root = build_tree(root_vals)
    p = TreeNode(p_val)
    q = TreeNode(q_val)

    sol = Solution()
    ancestor = sol.lowestCommonAncestor(root, p, q)
    return ancestor.val if ancestor else None

if __name__ == '__main__':
    # Example 1
    print("Example 1:")
    root_vals = [3,5,1,6,2,0,8,None,None,7,4]
    p_val, q_val = 5, 1
    print("LCA:", run_example(root_vals, p_val, q_val))  # Expected Output: 3

    # Example 2
    print("\nExample 2:")
    root_vals = [3,5,1,6,2,0,8,None,None,7,4]
    p_val, q_val = 5, 4
    print("LCA:", run_example(root_vals, p_val, q_val))  # Expected Output: 5

    # Example 3
    print("\nExample 3:")
    root_vals = [1,2]
    p_val, q_val = 1, 2
    print("LCA:", run_example(root_vals, p_val, q_val))  # Expected Output: 1
