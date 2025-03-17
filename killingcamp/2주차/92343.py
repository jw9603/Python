# 프로그래머스 양과 늑대
# https://school.programmers.co.kr/learn/courses/30/lessons/92343
from collections import defaultdict
def solution(info, edges):
    tree = defaultdict(list)
    for parent, child in edges:
        tree[parent].append(child)
    
    def dfs(node, sheep, wolf, possible_nodes):
        if info[node] == 0:
            sheep += 1
        else:
            wolf += 1
        
        if wolf >= sheep:
            return 0
        
        max_sheep = sheep
        
        next_nodes = possible_nodes[:]
        next_nodes.remove(node)
        next_nodes.extend(tree[node])
        
        for next_node in next_nodes:
            max_sheep = max(max_sheep, dfs(next_node, sheep, wolf, next_nodes))
        
        return max_sheep
    return dfs(0, 0, 0, [0])

if __name__ == '__main__':
    info1, edges1 = [0,0,1,1,1,0,1,0,1,0,1,1], [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]
    info2, edges2 = [0,1,0,1,1,0,1,0,0,1,0], [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]

    print(f"Result1: {solution(info=info1, edges=edges1)}")
    print(f"Result2: {solution(info=info2, edges=edges2)}")