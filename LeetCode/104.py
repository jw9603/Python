# 104. Maximum Depth of Binary Tree
# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/


from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    
    # 1. BFS
    def maxDepth_BFS(self,root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if root is None:
            return 0

        max_depth = 0
        q = deque()
        q.append((root,1))

        while q:
            cur_node,cur_depth = q.popleft()
            max_depth = max(max_depth, cur_depth)
            if cur_node.left:
                q.append((cur_node.left,cur_depth+1))
            if cur_node.right:
                q.append((cur_node.right,cur_depth+1))
        return max_depth
    
    # 2. Post Order
    def maxDepth_postorder(self,root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if root is None:
            return 0
        
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        
        max_depth = max(left,right) + 1
        return max_depth
    
    
    # 3. Pre Order
    def maxDepth_preorder(self,root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.max_depth = 0
        
        def pre_order(node, depth):
            if not node:
                return 0
            # Update max depth at each node
            self.max_depth = max(self.max_depth, depth)
            # Traverse the left and right children
            pre_order(node.left, depth + 1)
            pre_order(node.right, depth + 1)
        
        pre_order(root, 1)
        return self.max_depth
    
    # # 4. In Order
    def maxDepth_inorder(self,root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        
        self.max_depth = 0
        
        def in_order(node, depth):
            if not node:
                return 0
            
            # Traverse left subtree first
            in_order(node.left, depth + 1)
            
            # Process current node (update depth at the root)
            self.max_depth = max(self.max_depth, depth)
            
            # Traverse right subtree
            in_order(node.right, depth + 1)
        
        in_order(root, 1)
        return self.max_depth
        

def build_tree(nodes):
    if not nodes or nodes[0] is None:
        return None
    
    root = TreeNode(nodes[0])
    queue = deque([root])
    idx = 1
    
    while queue and idx < len(nodes):
        node = queue.popleft()
        
        # Left Child
        if idx < len(nodes) and nodes[idx] is not None:
            node.left = TreeNode(nodes[idx])
            queue.append(node.left)
        idx += 1
        
        # Right Child
        if idx < len(nodes) and nodes[idx] is not None:
            node.right = TreeNode(nodes[idx])
            queue.append(node.right)
        idx += 1
        
    return root

def run_example(root_vals):
    root = build_tree(root_vals)   
    sol = Solution()
    
    depth_bfs = sol.maxDepth_BFS(root)
    depth_postorder = sol.maxDepth_preorder(root)
    depth_preorder = sol.maxDepth_preorder(root)
    depth_inorder = sol.maxDepth_inorder(root)
    
    return depth_bfs, depth_postorder, depth_preorder, depth_inorder



if __name__ == '__main__':
    
    root_vals1 = [3,9,20,None,None,15,7]
    print('Example 1:')
    bfs, post_order, pre_order, in_order = run_example(root_vals1)
    print(f"Maximum Depth (BFS): {bfs}")
    print(f"Maximum Depth (Post-order): {post_order}")
    print(f"Maximum Depth (Pre-order): {pre_order}")
    print(f"Maximum Depth (In-order): {in_order}")
    
    root_vals2 = [1, None, 2]
    print('Example 2:')
    bfs, post_order, pre_order, in_order = run_example(root_vals2)
    print(f"Maximum Depth (BFS): {bfs}")
    print(f"Maximum Depth (Post-order): {post_order}")
    print(f"Maximum Depth (Pre-order): {pre_order}")
    print(f"Maximum Depth (In-order): {in_order}")
    
    
    
        
        
        
    
            