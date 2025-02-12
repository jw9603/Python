# LeetCode 200. Number of Islands
# https://leetcode.com/problems/number-of-islands/


############################# BFS #####################################
from collections import deque
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        cnt = 0
        m = len(grid)
        n = len(grid[0])
        visited = [[False] * n for _ in range(m)]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def bfs(x, y):
            visited[x][y] = True
            q = deque()
            q.append((x, y))
            
            while q:
                cur_x, cur_y = q.popleft()
                for direction in directions:
                    next_x = cur_x + direction[0]
                    next_y = cur_y + direction[1]

                    if 0 <= next_x < m and 0 <= next_y < n:
                        if grid[next_x][next_y] == '1' and not visited[next_x][next_y]:
                            visited[next_x][next_y] = True
                            q.append((next_x, next_y))
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not visited[i][j]:
                    bfs(i, j)
                    cnt += 1
        return cnt
       
############################# BFS #####################################

############################## DFS #####################################
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        cnt = 0
        m = len(grid)
        n = len(grid[0])
        visited = [[False] * n for _ in range(m)]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def dfs(x, y):
            visited[x][y] = True
            for direction in directions:
                next_x = x + direction[0]
                next_y = y + direction[1]

                if 0 <= next_x < m and 0 <= next_y < n:
                    if grid[next_x][next_y] == '1' and not visited[next_x][next_y]:
                        dfs(next_x, next_y)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not visited[i][j]:
                    dfs(i, j)
                    cnt += 1
        return cnt
############################## DFS #####################################
