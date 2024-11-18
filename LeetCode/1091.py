# 1091. Shortest path in binary matrix
# https://leetcode.com/problems/shortest-path-in-binary-matrix/description/

from collections import deque
class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

        result = -1
        m = len(grid)
        n = len(grid[0])
        if grid[0][0] != 0 or grid[m-1][n-1] != 0:
            return result
        queue = deque()
        queue.append((0,0,1))
        visited = [[False] * n for _ in range(m)]
        visited[0][0] = True

        while queue:
            cur_x, cur_y,cur_d = queue.popleft()

            if cur_x == m - 1 and cur_y == n - 1:
                result = cur_d
                break
            for dx, dy in directions:
                next_x = cur_x + dx
                next_y = cur_y + dy

                if 0 <= next_x and next_x < m and 0 <= next_y  and next_y < n:
                    if grid[next_x][next_y] == 0 and not visited[next_x][next_y]:
                        queue.append((next_x,next_y,cur_d+1))
                        visited[next_x][next_y] = True

    
        return result
    
if __name__ == '__main__':
    
    grid1 = [[0,1],[1,0]]
    grid2 = [[0,0,0],[1,1,0],[1,1,0]]
    grid3 = [[1,0,0],[1,1,0],[1,1,0]]
    
    a = Solution()
    
    print(a.shortestPathBinaryMatrix(grid1))
    print(a.shortestPathBinaryMatrix(grid2))
    print(a.shortestPathBinaryMatrix(grid3))