# 200. Number of islands
# https://leetcode.com/problems/number-of-islands/

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
    
        def bfs(x,y):
            dx = [-1,1,0,0]
            dy = [0,0,-1,1]
            visited[x][y] = True
            q = deque()
            q.append((x,y))
            while q:
                cur_x,cur_y = q.popleft()
                
                for r in range(4):
                    next_x = cur_x + dx[r]
                    next_y = cur_y + dy[r]
                    if 0 <= next_x and next_x < m and next_y >= 0 and next_y < n:
                        if grid[next_x][next_y] == '1' and not visited[next_x][next_y]:
                            visited[next_x][next_y] = True
                            q.append((next_x,next_y))
                    

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not visited[i][j]:
                    bfs(i,j)
                    cnt += 1
        return cnt
    
    
    def numIslands1(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        cnt = 0
        m = len(grid)
        n = len(grid[0])
        dx = [-1,1,0,0]
        dy = [0,0,-1,1]
        visited = [[False] * n for _ in range(m)]
        
        def dfs(x,y):
            visited[x][y] = True
            for i in range(4):
                next_x = x + dx[i]
                next_y = y + dy[i]
                if next_x >= 0 and next_x < m and next_y >= 0 and next_y < n:
                    if grid[next_x][next_y] == "1" and not visited[next_x][next_y]:
                        dfs(next_x, next_y)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not visited[i][j]:
                    dfs(i,j)
                    cnt += 1
        return cnt
                    
if __name__ == '__main__':
    
    grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
    grid2 = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
    
    sol = Solution()
    
    print('BFS')
    print(sol.numIslands(grid))
    print(sol.numIslands(grid2))
    
    print('DFS')
    print(sol.numIslands1(grid))
    print(sol.numIslands1(grid2))