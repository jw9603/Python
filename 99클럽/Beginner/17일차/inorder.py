class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def inorder_traversal_recursive(node):
    if node:
        inorder_traversal_recursive(node.left)
        print(node.value, end=' ')
        inorder_traversal_recursive(node.right)


if __name__ == '__main__':
    # 예제 트리 생성
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    # 전위 순회 호출
    inorder_traversal_recursive(root)