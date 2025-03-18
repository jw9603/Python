# LeetCode 1091. Shortest Path in Binary Matrix
# https://leetcode.com/problems/shortest-path-in-binary-matrix/description/
# https://leetcode.com/problems/shortest-path-in-binary-matrix/submissions/1577601273
from collections import deque
class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        visited = [[False] * n for _ in range(n)]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1

        queue = deque([(0, 0, 1)])

        while queue:
            cur_x, cur_y, cur_d = queue.popleft()

            if cur_x == n - 1 and cur_y == n - 1:
                return cur_d
            
            for dx, dy in directions:
                next_x, next_y = cur_x + dx, cur_y + dy

                if 0 <= next_x < n and 0 <= next_y < n:
                    if grid[next_x][next_y] == 0 and not visited[next_x][next_y]:
                        visited[next_x][next_y] = True
                        queue.append((next_x, next_y, cur_d + 1))
        return -1     
    
if __name__ == '__main__':
    grid1, grid2, grid3 = [[0, 1], [1, 0]], [[0,0,0],[1,1,0],[1,1,0]], [[1,0,0],[1,1,0],[1,1,0]]
    sol = Solution()
    print(f"Result1: {sol.shortestPathBinaryMatrix(grid=grid1)}")
    print(f"Result2: {sol.shortestPathBinaryMatrix(grid=grid2)}")
    print(f"Result3: {sol.shortestPathBinaryMatrix(grid=grid3)}")