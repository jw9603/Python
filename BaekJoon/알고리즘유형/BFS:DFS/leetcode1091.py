# Leetcode 1091. Shortest Path in Binary Matrix
# https://leetcode.com/problems/shortest-path-in-binary-matrix/description/

from collections import deque
class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        visited = [[False] * n for _ in range(n)]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (1, -1) ,(-1, 1), (-1 ,-1)]

        result = -1
        if grid[0][0] != 0  or grid[n - 1][n - 1] != 0:
            return result
        
        visited[0][0] = True
        queue = deque()
        queue.append((0, 0, 1))
        
        while queue:
            cur_x, cur_y, cur_d = queue.popleft()

            if cur_x == n -1 and cur_y == n - 1:
                result = cur_d
                break

            for dx, dy in directions:
                next_x = cur_x + dx
                next_y = cur_y + dy

                if 0 <= next_x < n and 0 <= next_y < n:
                    if grid[next_x][next_y] == 0 and not visited[next_x][next_y]:
                        visited[next_x][next_y] = True
                        queue.append((next_x, next_y, cur_d + 1))
        return result

if __name__ == '__main__':
    sol = Solution()
    result1 = sol.shortestPathBinaryMatrix([[0,1],[1,0]])
    result2 = sol.shortestPathBinaryMatrix([[0,0,0],[1,1,0],[1,1,0]])
    result3 = sol.shortestPathBinaryMatrix([[1,0,0],[1,1,0],[1,1,0]])
    print(result1)
    print(result2)
    print(result3)    
        