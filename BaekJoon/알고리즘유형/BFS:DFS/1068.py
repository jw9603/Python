# 백준 1068. 트리
# https://www.acmicpc.net/problem/1068
import sys
from collections import defaultdict
N = int(sys.stdin.readline().strip())
parents = list(map(int, sys.stdin.readline().split()))
delete_node = int(sys.stdin.readline().strip())

tree = defaultdict(list)
root = -1
for child, parent in enumerate(parents):
    if parent == -1:
        root = child
    else:
        tree[parent].append(child)


def count_leaf(node):
    if node == delete_node:
        return 0
    
    if node not in tree or all(child == delete_node for child in tree[node]):
        return 1
    
    leaf_cnt = 0
    for child_node in tree[node]:
        leaf_cnt += count_leaf(child_node)
    
    return leaf_cnt

if root == delete_node:
    print(0)
else:
    print(count_leaf(root))

    