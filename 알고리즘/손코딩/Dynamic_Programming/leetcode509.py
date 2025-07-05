# LeetCode 509. Fibonacci Number
# https://leetcode.com/problems/fibonacci-number/description/
# 1. Top-Down DP
class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo = {}
        def dfs(n):
            if n == 0:
                return 0
            if n == 1:
                return 1
            
            if n in memo:
                return memo[n]
            res = dfs(n - 1) + dfs(n - 2)
            memo[n] = res

            return memo[n]

        return dfs(n)
class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1] * (n + 1)
        if n == 0:
            return 0
        if n == 1:
            return 1
        dp[0], dp[1] = 0, 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
    
        return dp[n]