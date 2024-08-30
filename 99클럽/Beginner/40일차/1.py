class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n = len(cost)
        dp = [0] * n
        dp[0] = cost[0]
        dp[1] = cost[1]

        
        for i in range(2,n):
            dp[i] = cost[i] + min(dp[i-1],dp[i-2])

        
        return min(dp[n-1],dp[n-2])
    def minCostClimbingStairs1(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n = len(cost)

        for i in range(2,n):
            cost[i] += min(cost[i-1],cost[i-2])

        return min(cost[n-1],cost[n-2])
    
    
if __name__ == '__main__':
    
    import time
    
    t = time.time()
    
    a = Solution()
    res1 = a.minCostClimbingStairs([10,15,20])
    res2 = a.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1])
    
    print(f"Test Case1 Result: {res1}")
    print(f"Test Case2 Result: {res2}")
    
    print(f"{time.time()-t:.6f}초")
    
    
    
    t = time.time()
    
    a = Solution()
    res1 = a.minCostClimbingStairs1([10,15,20])
    res2 = a.minCostClimbingStairs1([1,100,1,1,1,100,1,1,100,1])
    
    print(f"Test Case1 Result: {res1}")
    print(f"Test Case2 Result: {res2}")
    
    print(f"{time.time()-t:.6f}초")
    
    