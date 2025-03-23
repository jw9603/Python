# 백준 1068. 트리
# https://www.acmicpc.net/problem/1068
import sys
from collections import defaultdict
def count_leaf(node):
    global delete_node, tree
    
    if node == delete_node:
        return 0

    if node not in tree or all(child == delete_node for child in tree[node]):
        return 1
    
    leaf_cnt = 0
    for next_node in tree[node]:
        leaf_cnt += count_leaf(next_node)

    return leaf_cnt

def main():
    global delete_node, tree
    N = int(sys.stdin.readline().strip())
    parents = list(map(int, sys.stdin.readline().split()))
    delete_node = int(sys.stdin.readline().strip())

    tree = defaultdict(list)
    for child, parent in enumerate(parents):
        if parent == -1:
            root = child
        else:
            tree[parent].append(child)

    if root == delete_node:
        print(0)
    else:
        print(count_leaf(root))

if __name__ == '__main__':
    main()