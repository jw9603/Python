# 62. Unique Paths
# https://leetcode.com/problems/unique-paths/description/

class Solution(object):
    
    # # 1. 완전 탐색
    def uniquePaths(self, m, n): # O(2^(m+n))
        # https://leetcode.com/problems/unique-paths/submissions/1458968943
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        
        def move(x, y):
            if x == 0 and y == 0:
                return 1
            
            paths = 0
            
            if x - 1 >= 0:
                paths += move(x - 1, y)
            if y - 1 >= 0:
                paths += move(x, y - 1)
            
            return paths
        
        return move(m - 1, n - 1)
        
    # # 2. Combinations
    def uniquePaths(self, m, n): # O(m + n)
        # https://leetcode.com/problems/unique-paths/submissions/1458969323
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        from math import factorial
        def comb(x,y): # xCr = x! / (x-y)! * y!
            return factorial(x) // (factorial(x - y) * factorial(y))
        return comb(m + n - 2, m - 1)
    
    # 3. Top-Down dp dict
    def uniquePaths(self, m, n): # O(m * n)
        # https://leetcode.com/problems/unique-paths/submissions/1458969837
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        memo = {}
        
        def dp(x, y):
            if x == 0 and y == 0:
                memo[(x,y)] = 1
                return memo[(x,y)]
            
            if (x,y) in memo:
                return memo[(x,y)]
            
            paths = 0
            
            if x - 1 >= 0:
                paths += dp(x - 1, y)
            if y - 1 >= 0:
                paths += dp(x, y - 1)
            memo[(x,y)] = paths
            
            return memo[(x,y)]
        
        return dp(m - 1, n - 1)
    
    # 4. Top-Down dp list
    def uniquePaths(self, m, n): # O(m*n)
        # https://leetcode.com/problems/unique-paths/submissions/1458967118
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
    
    # # 5. Bottom-Up dp
    def uniquePaths(self, m, n): # O(m*n)
        # https://leetcode.com/problems/unique-paths/submissions/1458968642
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
            
        for r in range(1,m):
            for c in range(1,n):
                memo[r][c] = memo[r - 1][c] + memo[r][c - 1]
                
        return memo[m - 1][n - 1]
        
        
    
if __name__ == '__main__':
    a = Solution()
    
    print(a.uniquePaths(3,7))
    print(a.uniquePaths(3,2))
    
    