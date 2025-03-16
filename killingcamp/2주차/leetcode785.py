# LeetCode 785. Is Graph Bipartite?
# https://leetcode.com/problems/is-graph-bipartite/description/
# 1. BFS
# https://leetcode.com/problems/is-graph-bipartite/submissions/1575616580
from collections import deque
class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        n = len(graph)
        color = [0] * n # 0: 방문 안 함, 1 or -1: 두 개의 그룹

        def bfs(start):
            queue = deque([start])
            color[start] = 1

            while queue:
                cur_node = queue.popleft()

                for next_node in graph[cur_node]:
                    if color[next_node] == 0:
                        color[next_node] = - color[cur_node]
                        queue.append(next_node)
                    elif color[next_node] == color[cur_node]:
                        return False
            return True


        for i in range(n):
            if color[i] == 0:
                if not bfs(i):
                    return False
        return True     
# 2. DFS
# https://leetcode.com/problems/is-graph-bipartite/submissions/1575624208
class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        n = len(graph)
        color = [0] * n # 0: 방문 안 함, 1 or -1: 두 개의 그룹

        def dfs(start, c):
            color[start] = c

            for next_node in graph[start]:
                if color[next_node] == 0:
                    if not dfs(next_node, -c):
                        return False
                elif color[next_node] == color[start]:
                    return False
            return True

        for i in range(n):
            if color[i] == 0:
                if not dfs(i, 1):
                    return False
        return True
    
if __name__ == '__main__':
    graph1, graph2 = [[1,2,3],[0,2],[0,1,3],[0,2]], [[1,3],[0,2],[1,3],[0,2]]
    sol = Solution()
    print(f"Result1: {sol.isBipartite(graph=graph1)}")
    print(f"Result2: {sol.isBipartite(graph=graph2)}")