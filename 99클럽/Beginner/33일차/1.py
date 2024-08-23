# Leetcode 1530. Number of Good Leaf Nodes Pairs
    

############################ DFS (stack) ##############################
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self,val=0,left=None,right=None):
        self.val =val
        self.left = left
        self.right = right
        
from collections import deque

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def countPairs(self, root, distance):
        """
        :type root: TreeNode
        :type distance: int
        :rtype: int
        """
        if not root:
            return 0

        result = 0
        stack = deque([(root, False)])
        node_to_distances = {}

        while stack:
            node, visited = stack.pop()
            if not node:
                continue
            
            if visited:  # 노드를 다시 방문했을 때 (후위 순회)
                if not node.left and not node.right:  # 리프 노드인 경우
                    node_to_distances[node] = [1]  # 리프 노드는 자기 자신과의 거리가 1
                else:
                    distances = []
                    if node.left:
                        left_distances = node_to_distances[node.left]
                    else:
                        left_distances = []
                    if node.right:
                        right_distances = node_to_distances[node.right]
                    else:
                        right_distances = []

                    # 유효한 리프 노드 쌍의 개수를 세기
                    for l in left_distances:
                        for r in right_distances:
                            if l + r <= distance:
                                result += 1
                    
                    # 현재 노드의 거리 정보 업데이트
                    for d in left_distances + right_distances:
                        if d + 1 <= distance:
                            distances.append(d + 1)
                    node_to_distances[node] = distances

            else:
                stack.append((node, True))  # 노드를 다시 방문할 때를 표시
                if node.right:
                    stack.append((node.right, False))
                if node.left:
                    stack.append((node.left, False))
        
        return result
############################ DFS (stack) ##############################

############################ DFS (재귀) #################################

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self,val=0,left=None,right=None):
        self.val =val
        self.left = left
        self.right = right
class Solution(object):
    def countPairs(self, root, distance):
        """
        :type root: TreeNode
        :type distance: int
        :rtype: int
        """
        self.result = 0
        
        def dfs(node):
            if not node:
                return []
            # If it's a leaf node
            if not node.left and not node.right:
                return [1] # Distance 1 to itself

            left_distances = dfs(node.left)
            right_distances = dfs(node.right)
            
            # Count all valid pairs
            for l in left_distances:
                for r in right_distances:
                    if l + r <= distance:
                        self.result += 1
            
            # Return distances to this node's parent
            return [d + 1 for d in left_distances + right_distances if d + 1 <= distance]
        
        dfs(root)
        return self.result
############################ DFS (재귀) #################################       