# LeetCode 62. Unique paths
# https://leetcode.com/problems/unique-paths/description/
# 1. Brute-Force
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        def move(x, y):
            # 1. base case
            if x == 0 and y == 0:
                return 1
            
            paths = 0
            if x - 1 >= 0:
                paths += move(x - 1, y)
            if y - 1 >= 0:
                paths += move(x, y - 1)
            return paths
        return move(m - 1, n - 1)

# 2. Top-Down
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        memo = {}
        def dp(x, y):
            # 1. base case
            if x == 0 and y == 0:
                memo[(x, y)] = 1
                return memo[(x, y)]
            
            if (x, y) in memo:
                return memo[(x, y)]
            
            paths = 0
            if x - 1 >= 0:
                paths += dp(x - 1, y)
            if y - 1 >= 0:
                paths += dp(x, y - 1)
            memo[(x, y)] = paths
            return memo[(x, y)]
        return dp(m - 1, n - 1)
# 3. Top-Down-list
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        memo = [[-1] * n for _ in range(m)]

        def dp(x, y):
            if x == 0 and y == 0:
                memo[x][y] = 1
                return memo[x][y]
            
            if memo[x][y] != -1:
                return memo[x][y]
            
            paths = 0
            if x - 1 >= 0:
                paths += dp(x - 1, y)
            if y - 1 >= 0:
                paths += dp(x, y - 1)
            memo[x][y] = paths
            return memo[x][y]
        return dp(m - 1, n - 1)

# 4. Bottom-Up
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        memo = [[-1] * n for _ in range(m)]

        for r in range(m):
            memo[r][0] = 1
        for c in range(n):
            memo[0][c] = 1

        for r in range(1, m):
            for c in range(1, n):
                memo[r][c] = memo[r - 1][c] + memo[r][c - 1]
        return memo[m - 1][n - 1]