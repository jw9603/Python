# 70. Climbing Stairs
# https://leetcode.com/problems/climbing-stairs/description/

class Solution(object):
    # Top-down
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        memo = {}
        def dp(n):
            if n == 0 or n == 1:
                return 1
            if n in memo:
                return memo[n]
            memo[n] = dp(n - 1) + dp(n - 2)
            
            return memo[n]
        
        return dp(n)
    
    # # Bottom-Up
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        case = [1] * (n + 1)
        
        for i in range(2,n+1):
            case[i] = case[i -1] + case[i - 2]
            
        return case[n]
    
    # Bottom-Up-optimized
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        a, b = 1, 1
        for _ in range(2,n+1):
            a, b = b, a + b
        return b
        

if __name__ == '__main__':
    
    a = Solution()
    
    print(a.climbStairs(2))
    print(a.climbStairs(3))
    print(a.climbStairs(7))