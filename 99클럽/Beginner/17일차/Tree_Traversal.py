# 전위 순회 => 현재 노드 -> 좌 서브트리 -> 우 서브트리
def preorder(node):
    if node != ".":
        preorder.order += node
        preorder(tree[node][0])
        preorder(tree[node][1])

# 중위 순회 => 좌 서브트리 -> 현재 노드 -> 우 서브트리
def inorder(node):
    if node != ".":
        inorder(tree[node][0])
        inorder.order += node
        inorder(tree[node][1])

# 후위 순회 => 좌 서브트리 -> 우 서브트리 -> 현재 노드
def postorder(node):
    if node != ".":
        postorder(tree[node][0])
        postorder(tree[node][1])
        postorder.order += node

if __name__ == "__main__":
    tree = {
    "A": ("B", "C"),
    "B": ("D", "E"),
    "C": ("F", "G"),
    "D": (".", "."),
    "E": (".", "."),
    "F": (".", "."),
    "G": (".", "."),
    }
    """
        A
       / \
      B   C
     / \ / \
    D  E F  G
    """

    preorder.order, inorder.order, postorder.order = "", "", ""
    preorder("A")  # ABDECFG
    inorder("A")   # DBEAFCG
    postorder("A") # DEBFGCA
    print(preorder.order, inorder.order, postorder.order, sep="\n")