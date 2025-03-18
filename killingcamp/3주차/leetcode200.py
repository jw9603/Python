# LeetCode 200. Number of Islands
# https://leetcode.com/problems/number-of-islands/
# 1. BFS
# https://leetcode.com/problems/number-of-islands/submissions/1577570942
from collections import deque
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        
        def bfs(x, y):
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            queue = deque([(x, y)])

            while queue:
                cur_x, cur_y = queue.popleft()

                for dx, dy in directions:
                    next_x, next_y = cur_x + dx, cur_y + dy

                    if 0 <= next_x < m and 0 <= next_y < n:
                        if grid[next_x][next_y] == "1" and not visited[next_x][next_y]:
                            visited[next_x][next_y] = True
                            queue.append((next_x, next_y))
        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and not visited[i][j]:
                    bfs(i, j)
                    cnt += 1
        return cnt  

# 2. DFS
# https://leetcode.com/problems/number-of-islands/submissions/1577573455
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]

        def dfs(x, y):
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            visited[x][y] = True

            for dx, dy in directions:
                next_x, next_y = x + dx, y + dy

                if 0 <= next_x < m and 0 <= next_y < n:
                    if grid[next_x][next_y] == "1" and not visited[next_x][next_y]:
                        dfs(next_x, next_y)

        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and not visited[i][j]:
                    dfs(i, j)
                    cnt += 1
        return cnt
    
if __name__ == '__main__':
    grid1 = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
    grid2 = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]

    sol = Solution()

    print(f"Result1: {sol.numIslands(grid=grid1)}")
    print(f"Result1: {sol.numIslands(grid=grid2)}")