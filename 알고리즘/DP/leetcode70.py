# LeetCode 70. Climbing Stairs
# https://leetcode.com/problems/climbing-stairs/
# 1. 완전 탐색
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 1. base case
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        res = self.climbStairs(n - 1) + self.climbStairs(n - 2)

        return res

# 2. Top-Down
class Solution(object):

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo = {}
        def dp(n):
            if n == 1:
                return 1
            if n == 2:
                return 2
            if n in memo:
                return memo[n]

            res = dp(n - 1) + dp(n - 2)
            memo[n] = res

            return memo[n]
        
        return dp(n)

# 3. Bottom-Up
class Solution(object):

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        tab = [0] * (n + 1)

        if n == 1:
            return 1
        if n == 2:
            return 2

        tab[1] = 1
        tab[2] = 2

        for i in range(3, n + 1):
            tab[i] = tab[i - 1] + tab[i - 2]
        
        return tab[n]