# 746. Min Cost Climbing Stairs
# https://leetcode.com/problems/min-cost-climbing-stairs/description/

class Solution(object):
    # Top-Down
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        memo = {}
        
        def dp(n):
            if n == 0 or n == 1:
                return 0
            if n in memo:
                return memo[n]
            memo[n] = min(dp(n - 1) + cost[n - 1], dp(n - 2) + cost[n - 2])
            
            return memo[n]
        
        return dp(len(cost))
        
    # # Bottom-up
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n = len(cost)
        dp = [0] * (n + 1)
        
        for i in range(2,n + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
            
        return dp[n]
        
        
if __name__ == '__main__':
    
    a = Solution()
    
    print(a.minCostClimbingStairs([10,15,20]))
    print(a.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))
    
    