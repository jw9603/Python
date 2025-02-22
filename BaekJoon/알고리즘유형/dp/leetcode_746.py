# LeetCode 746. Min Cost Climbing Stairs
# https://leetcode.com/problems/min-cost-climbing-stairs/description/

# 1. Top-Down
class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        memo = {}
        def dp(n):
            # 1. base case
            if n == 0 or n == 1:
                return 0
            
            if n in memo:
                return memo[n]
            
            memo[n] = min(dp(n - 1) + cost[n - 1], dp(n - 2) + cost[n - 2])
            return memo[n]
        return dp(len(cost))
# 2. Bottom-Up
class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        tab = [-1] * (len(cost) + 1)
        tab[0], tab[1] = 0, 0

        for i in range(2, len(cost) + 1):
            tab[i] = min(tab[i - 1] + cost[i - 1], tab[i - 2] + cost[i - 2])
        return tab[len(cost)]

        