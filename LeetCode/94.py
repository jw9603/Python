# 94. Tree Tree Inorder Traversal
# https://leetcode.com/problems/Tree-tree-inorder-traversal/

# Definition for a Tree tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    # 1. Recursive
    def inorderTraversal1(self, root):
        # https://leetcode.com/problems/Tree-tree-inorder-traversal/submissions/1473951557
        # Inorder traversal : 중위 순회로, 왼 -> root -> 오
        """
        :type root: TreeNode
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
    # 2. stack
    def inorderTraversal2(self, root):
        # https://leetcode.com/problems/Tree-tree-inorder-traversal/submissions/1473955911
        """
        :type root: TreeNode
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

if __name__ == '__main__':
    a = Solution()

    bt = TreeNode()
    bt.root = TreeNode(val=1)
    bt.root.left = TreeNode(val=2)
    bt.root.right = TreeNode(val=3)
    bt.root.left.left = TreeNode(val=4)
    bt.root.left.right = TreeNode(val=5)
    bt.root.right.right = TreeNode(val=6)
    
    
    print(f"using recursive method: {a.inorderTraversal1(bt.root)}")
    print(f"using stack method: {a.inorderTraversal2(bt.root)}")
    
