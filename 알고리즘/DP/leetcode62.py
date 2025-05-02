# LeetCode 62. Unique Paths
# https://leetcode.com/problems/unique-paths/
# 1. Brute Force
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        def move(r, c):
            # 1. base case
            if r == 0 and c == 0:
                return 1
            paths = 0

            if r - 1 >= 0:
                paths += move(r - 1, c)
            if c - 1 >= 0:
                paths += move(r, c - 1)
            
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
        tab = {}

        def dp(r, c):
            if r == 0 and c == 0:
                tab[(r, c)] = 1
                return tab[(r, c)]
            
            paths = 0
            if r - 1 >= 0:
                paths += dp(r - 1, c)
            if c - 1 >= 0:
                paths += dp(r, c - 1)
            
            tab[(r, c)] = paths

            return tab[(r, c)]
        
        return dp(m - 1, n - 1)

# 3. Bottom-Up
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