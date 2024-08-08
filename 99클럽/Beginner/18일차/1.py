# https://leetcode.com/problems/increasing-order-search-tree/
# 897. Increasing Order Search Tree

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
  def increasingBST(self, root):
    if not root:
        return    
    def inorder(root,res):
        if not root:
            return
        inorder(root.left,res)
        res.append(root.val)
        inorder(root.right,res)
        return res
    array = inorder(root,[])
    new_root = TreeNode(array[0])
    current = new_root
    for i in range(1,len(array)):
        current.right = TreeNode(array[i])
        current = current.right
    
    return new_root


# Helper function to print the tree in order
def print_tree(root):
    current = root
    while current:
        print(current.val, end=" -> ")
        current = current.right
    print("Done")

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.left.left.left = TreeNode(1)
root.right.right = TreeNode(8)
root.right.right.left = TreeNode(7)
root.right.right.right = TreeNode(9)



# Create the solution object
solution = Solution()

# Get the result of increasingBST
result = solution.increasingBST(root)

# Print the result
print_tree(result)
